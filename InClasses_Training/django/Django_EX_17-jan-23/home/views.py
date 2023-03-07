from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from django.views import View
from datetime import date

from .models import Invoice

import pdfkit

# Create your views here.

# http://127.0.0.1:8000/?location=Berlin&other1=has&other2=nice weather


@csrf_exempt
def home(request):
    if request.method == "GET":
        my_crazy_string = ""
        for key, value in request.GET.items():
            my_crazy_string += str(value) + " "
        return HttpResponse(f"Hello class! {my_crazy_string}")
    elif request.method == "POST":
        file = request.FILES.get("data")
        print(request.FILES, file)
        print(dir(request.session))
        # print(request.META)
        return HttpResponse("You are posting ", file)
    else:
        return HttpResponse(f"What the heck happened? You used {request.method}")


@csrf_exempt
def download(request):
    """Download a invoice file."""

    # create fake data
    invoice_of_user = Invoice(
        invoice_num=4892,
        name="Some guy",
        address="101 E. Chapman Ave<br>Orange, CA 92866",
        phone="(800) 555-1234",
        price=500,
    )

    # build the context dict
    context = {"invoice": invoice_of_user, "date": date.today()}
    # render template
    template = get_template("create_invoice.html")
    # build html
    html = template.render(context)
    filename = "invoice.pdf"
    # build pdf object
    pdf = pdfkit.from_string(html, False)
    # build response object
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="' + filename + '"'
    return response






    def post(self, request, *args, **kwargs):
        pass
