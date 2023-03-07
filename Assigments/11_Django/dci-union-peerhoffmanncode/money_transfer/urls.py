
from django.urls import path

from . import views

urlpatterns = [
    path("", views.SendMoney.as_view(), name = "send"),
    path("show/", views.ShowTransaction.as_view(), name = "show"),
]
