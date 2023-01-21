from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def base_view(request):
    return render(request, "myapp/base.html")


class AboutView(TemplateView):
    template_name = "myapp/about.html"
