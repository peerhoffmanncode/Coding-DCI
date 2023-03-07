from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    This is some sample documentation which you can see in the browser
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'photo', 'price']

    # we can modify the serializer as follows as well
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['is_on_sale'] = instance.on_sale()
        return data

    # Check in the django shell    