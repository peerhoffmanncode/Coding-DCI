from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.urls import reverse_lazy
import datetime
from email.message import EmailMessage
import ssl, smtplib, os
from django.core.mail import send_mail

from .forms import SearchForm, HotelSearch, CarSearch, ContactForm

# class Browse(FormView):
#     template_name = "shop/index.html"
#     form_class = SearchForm

#     # customize initial values
#     def get_initial(self):

#         return {"search_term": "Another title"}


# Original Code
# class Browse(TemplateView):
#     template_name = "shop/index.html"
#     def get_context_data(self, *args, **kwargs):
#         return {
#             "form": SearchForm(),
#             "hotel": HotelSearch(),
#             "car": CarSearch(),
#             "contact": ContactForm()
#         }

# ALso on slack!!!# Slide 38
password = os.getenv('PASSWORD')
email_sender = 'vicmiclovich@gmail.com'
email_receiver = 'vicmiclovich@gmail.com'

class Browse(FormView):
    template_name = "shop/index.html"
    form_class = ContactForm
    success_url = reverse_lazy("success")

    # handle the POST request
    def post(self, request):   
        response = super().post(request) # use someone else's logic!

        form = ContactForm(request.POST)
        # 1) extract the email, name and reason (use variables to store them)
        if form.is_valid(): # -> False
            email = form.data.get('email')
            name = form.data.get('name')
            reason = form.data.get('reason')
        else:
            render(request, 'shop/index.html', {'errors': "Sorry you have an error"})
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
