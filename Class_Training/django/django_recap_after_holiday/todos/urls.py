
from django.urls import path

from .views import index as landing_page

urlpatterns = [
    path("", landing_page, name = "landing_page"),
]
