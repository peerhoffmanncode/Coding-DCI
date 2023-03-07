from django.urls import path
from django.contrib import admin
from .views import show, cart, index, ProductList, ProductCreate, ProductDelete

urlpatterns = [
    path("api/v1/products/", ProductList.as_view()),
    path("api/v1/products/create/", ProductCreate.as_view()),
    path("api/v1/products/delete/<int:pk>", ProductDelete.as_view()),
    path("products/<int:pk>/", show, name="product-detail"),
    path("cart/", cart, name="cart"),
    path("admin/", admin.site.urls),
    path("", index, name="product-list"),
]
