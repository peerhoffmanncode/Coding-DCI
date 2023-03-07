from django.urls import path, re_path, register_converter
from .views import phone_number_validation

from .converter import PhoneNumberConverter

register_converter(PhoneNumberConverter, 'ph')

urlpatterns = [
    path('phone/<ph:phone_number>', phone_number_validation),
]
