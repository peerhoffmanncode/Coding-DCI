from django.shortcuts import render
from django.views.generic.edit import FormView

# Create your views here.
from .forms import ZodiacForm

import requests


class HoroscopeCreateView(FormView):
    template_name = "horror/horoscope.html"
    form_class = ZodiacForm

    def post(self, request, *args: str, **kwargs):

        selected_sign = request.POST.get("select")
        url = f"https://ohmanda.com/api/horoscope/{selected_sign}"
        context = requests.get(url).json()

        return render(request, "horror/show.html", context)
