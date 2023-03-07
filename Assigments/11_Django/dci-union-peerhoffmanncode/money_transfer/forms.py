from django import forms

# from iso3166 import countries
# for country in countries:
#     CHOICES_COUNTRIES = (str(country[0].lower()), str(country[0]))

from  django.conf import settings


class MoneySendForm(forms.Form):

    sending_country = forms.ChoiceField(choices=settings.CHOICES_COUNTRIES, required=True, label="Your country", initial='Germany')
    sending_country_cur = forms.ChoiceField(choices=settings.CHOICES_CURRENCIES, required=True, label="Your currency", initial='EUR')
    receiving_country = forms.ChoiceField(choices=settings.CHOICES_COUNTRIES, required=True, label="Recipient's country", initial='Germany')
    receiving_country_cur = forms.ChoiceField(choices=settings.CHOICES_CURRENCIES, required=True, label="Recipient's currency", initial='EUR')
    money_amount = forms.FloatField(required=False, initial='0')
