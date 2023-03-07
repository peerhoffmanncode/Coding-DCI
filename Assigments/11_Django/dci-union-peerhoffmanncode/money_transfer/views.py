from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from .forms import MoneySendForm
import pycountry
from countryinfo import CountryInfo

from forex_python.converter import CurrencyRates, CurrencyCodes

class SendMoney(FormView):
    template_name = 'money_transfer/send_transfer.html'
    form_class = MoneySendForm


    def post(self, request, *args, **kwargs):
        form = MoneySendForm(request.POST)
        if form.is_valid():
            sender_country = pycountry.countries.lookup(form.cleaned_data["sending_country"])
            receiver_country = pycountry.countries.lookup(form.cleaned_data["receiving_country"])
            sender_currency = pycountry.currencies.lookup(form.cleaned_data["sending_country_cur"])
            receiver_currency = pycountry.currencies.lookup(form.cleaned_data["receiving_country_cur"])

            conversion_rate_for_sender = CurrencyRates().get_rates(sender_currency.alpha_3)
            sender_cur_sym = CurrencyCodes().get_symbol(sender_currency.alpha_3)
            receiver_cur_sym = CurrencyCodes().get_symbol(receiver_currency.alpha_3)

            conversion_rate = conversion_rate_for_sender.get(receiver_currency.alpha_3, 1.0)

            context = {
                "sender_country": sender_country,
                "sender_currency": sender_currency,
                "sender_currency_sym": sender_cur_sym,
                "receiver_country": receiver_country,
                "receiver_currency": receiver_currency,
                "receiver_currency_sym": receiver_cur_sym,
                "money_amount": round((conversion_rate * form.cleaned_data["money_amount"]),2),
                "conversion_rate": str(round(conversion_rate,5)).replace(".", ",")
                }
            return render(request, 'money_transfer/show_transfer.html', context)
        return redirect(reverse('send'))

class ShowTransaction(TemplateView):
    pass
