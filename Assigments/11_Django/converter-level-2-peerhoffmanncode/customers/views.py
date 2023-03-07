from django.shortcuts import render


def phone_number_validation(request, phone_number):
    context = {"phone_number": phone_number}
    return render(request, "customers/valid.html", context)
