"""stuff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home, download
from shop.views import Browse, Index, Product

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("download/", download, name="download"),
    path("shop/", Index.as_view(), name="index"),
    path("shop/product", Product.as_view(), name="product"),
    path("shop/browse", Browse.as_view(), name="browse"),
]
