from django.shortcuts import render
from .models import Product, Cart
from .serializer import ProductSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
# exceptions for what might happen when creating a new value
from rest_framework.exceptions import ValidationError

def show(request, pk):
    context = {"product": Product.objects.get(pk=pk)}
    return render(request, "shop/product.html", context)


def cart(request):
    context = {
        "items": [],
        "subtotal": 1,
        "tax_rate": int(Cart.TAX_RATE * 100),
        "tax_total": 2.0,
        "total": 3,
    }
    return render(request, "shop/cart.html", context)


def index(request):
    return render(
        request, "shop/product_list.html", {"products": Product.objects.all()}
    )


# API code

class PaginatedProducts(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100 # maximum size of the page that can be set by the API client

class ProductList(ListAPIView):
    """
    In many cases you want to use the restframework generic views
    because of ease.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    # Partial Match is a default matcher being used - it looks for
    # text that is case insensitive (upper or lower case it does not matter)
    # You can use Exact Match or Regular expressions
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('id', )
    search_fields = ('name', 'description')
    pagination_class = PaginatedProducts

    # something more complex (filter whether a product is on sale or not!)
    def get_queryset(self):
        # TODO: You can check the parameters and do some custom work
        # self.request.query_params.get(??, ??)
        return super().get_queryset()


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer

    # override create method
    def create(self, request, *args, **kwargs):
        try:
            # the validation here will prevent anyone using the API from
            # creating a free product
            price = request.data.get('price')
            if not price and float(price) <= 0.0:
                raise ValidationError({'price': "Must be above €0.0"})
        except ValueError:
            raise ValidationError({'price': "Price must be a number"})
        return super().create(request, *args, **kwargs)


class ProductDelete(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
