from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from .forms import CarSearch, SearchForm, HotelSearch
from datetime import datetime

# Create your views here.


# class Browse(View):
#     text = "Hello DIC"

#     def get(self, request, *args, **kwargs):
#         current_minute = datetime.now().minute
#         if current_minute % 2 == 0:
#             self.text = "The minute is even"
#         else:
#             self.text = "The minute is odd"

#         context = {
#             "form":SearchForm
#         }

#         return


class Browse(FormView):
    template_name = "shop/index.html"

    def get_context_data(self, **kwargs) -> dict:
        return {
            "form1": CarSearch,
            "form2": SearchForm,
            "form3": HotelSearch,
        }


class Index(TemplateView):
    template_name = "shop/index.html"


class Product(TemplateView):
    template_name = "shop/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_title"] = "Shoes"
        context["price"] = "49"
        return context
