from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Url
from .forms import UrlForm

import django.core.exceptions
import random

from datetime import date


def get_random_string(char_num) -> str:
    # dump random string
    source = "ABCDEFEGHIZKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    while True:
        rnd_str = "".join(
            [source[random.randint(0, len(source) - 1)] for i in range(char_num)]
        )
        try:
            url = Url.objects.get(short_url=rnd_str)
        except:
            break

    return rnd_str


# Create your views here.
class ShortageView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = UrlForm()
        return render(request, "shortener/url_input.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        if form.is_valid():
            source_shorten = form.cleaned_data["source_url"]
            shortened_url = get_random_string(6)
            short_url = Url.objects.create(
                source_url=source_shorten, short_url=shortened_url
            )
            request.session["short_url_pk"] = short_url.pk
            return redirect(reverse("result"))
        else:
            if (
                type(form.errors.as_data()["source_url"][0])
                == django.core.exceptions.ValidationError
            ):
                short_url = get_object_or_404(
                    Url, source_url=form.data.get("source_url", None)
                )
                request.session["short_url_pk"] = short_url.pk
                return redirect(reverse("result"))

        return redirect(reverse("shortage"))


class Result(TemplateView):
    def get(self, request, *args, **kwargs):
        # get url from session -> get from db
        if request.session.get("short_url_pk"):
            url = get_object_or_404(Url, pk=request.session.get("short_url_pk"))
            return render(request, "shortener/result.html", {"url": url})
        return redirect(reverse("shortage"))


class RestoreView(TemplateView):
    def get(self, request, *args, **kwargs):
        url_to_restore = kwargs["surl"]
        restored_url = get_object_or_404(Url, short_url=url_to_restore)
        if restored_url.expires > date.today():
            return redirect(restored_url.source_url)
        else:
            exp_date = restored_url.expires
            restored_url.delete()
            return render(request, "shortener/expired.html", {"expired": exp_date})
