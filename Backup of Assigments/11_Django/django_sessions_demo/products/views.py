from django.shortcuts import render
from .models import Product

from pprint import pprint

def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def details(request, pk):
    product = Product.objects.get(pk=pk)
    ip = str(get_ip_address(request))
    key = "site_visits_"+str(product)

    if not request.session.get('visits', None):
        request.session['visits'] = {}

    if not request.session['visits'].get(ip, None):
        request.session['visits'][ip] = {}

    if not request.session['visits'][ip].get(key):
        request.session['visits'][ip][key] = 0

    request.session['visits'][ip][key] += 1
    request.session.save()

    visits = request.session['visits'][ip][key]

    return render(request, "products/details.html", {"product": product, "visits": visits})
