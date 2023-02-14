from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import SearchForm, HotelSearch, CarSearch, ContactForm

from django.core.mail import send_mail
from django.conf import settings

from pprint import pprint


class Browse(FormView):
    template_name = "shop/index.html"
    form_class = ContactForm
    success_url = reverse_lazy("success")

    def form_valid(self, form):
        if "wtf" in form.data.get("email"):
            return super().form_invalid(form)
        return super().form_valid(form)


    # handle the POST request
    def post(self, request):
        response = super().post(request) # use someone else's logic!
        form = ContactForm(request.POST)

        # 1) extract the email, name and reason (use variables to store them)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            full_msg = form.cleaned_data['reason']

            email_from = settings.EMAIL_HOST_USER
            reciepient_list = [email,]
            subject = f"[{name}] sends: Some crazy mail for you - prove of concept !"
            send_mail (subject, full_msg, email_from, reciepient_list)

        return response


class Product(TemplateView):
    template_name = "shop/product.html"
    # TODO: add a context variable that has the following
    # { "product_title": "Shoes", "price": 49 }
    # show this in the the shop/product.html
    def get_context_data(self, **kwargs):
        return {
            "product_title": "Shoes",
            "price": 49
        }
