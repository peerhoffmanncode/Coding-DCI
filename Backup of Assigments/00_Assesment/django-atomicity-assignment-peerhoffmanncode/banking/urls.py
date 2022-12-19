from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("add-customer/", views.add, name="add"),
    path("transfer/", views.transfer, name="transfer"),
]
