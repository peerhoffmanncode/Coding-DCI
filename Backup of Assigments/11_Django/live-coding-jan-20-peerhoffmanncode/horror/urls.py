from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.HoroscopeCreateView.as_view(), name="horoscope"),
]
