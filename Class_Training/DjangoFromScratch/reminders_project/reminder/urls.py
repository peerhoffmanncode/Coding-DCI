from django.urls import path

from . import views

urlpatterns = [
    path("", views.homer, name="index"),
    path("add/", views.bart, name="add"),
    path("<int:pk>/update/", views.lisa, name="update"),
    path("<int:pk>/delete/", views.barny, name="delete"),
]
