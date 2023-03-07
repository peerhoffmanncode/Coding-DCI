from django.shortcuts import render

from django.http import HttpResponse
import logging

# Create your views here.

logger = logging.getLogger(__name__)


def hello_world(request):
    # division = x / 100
    logger.warning("I am teapot")
    return HttpResponse(f"Hello world")
