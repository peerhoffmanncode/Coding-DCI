from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    # create a range of numbers (0-2000)
    numbers = range(1, 2000 + 1)

    # template context "variable"
    context = {"numbers": numbers}
    return render(request, "home/index.html", context)


def hello_json(request):
    # return a json dict with:
    # name: your name
    return JsonResponse({"name": "peer"})
