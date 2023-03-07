from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import FormView
from django.http import HttpResponse
import datetime
from .forms import SearchForm, HotelSearch, CarSearch, ContactForm

# class Browse(FormView):
#     template_name = "shop/index.html"
#     form_class = SearchForm


# Original Code
# class Browse(TemplateView):
#     template_name = "shop/index.html"

#     def get_context_data(self, *args, **kwargs):
#         return {
#             "form": SearchForm(),
#             "hotel": HotelSearch(),
#             "car": CarSearch(),
#             "contact_form": ContactForm()
#         }

class Browse(FormView):
    template_name = "shop/index.html"
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def post(self, request, *args, **kwargs):
        response = super().post(request
        form = ContactForm(request.POST)
        if form.is_valid():








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
