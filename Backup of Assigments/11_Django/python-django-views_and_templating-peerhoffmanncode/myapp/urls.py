from django.contrib import admin
from django.urls import path

from myapp.views import base_view, AboutView

urlpatterns = [
    path("", base_view, name="base"),
    path("about/", AboutView.as_view(), name="about"),
]
