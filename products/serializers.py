from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerilizer):
    class Meta:
        model = Product
        fields = '__all__'
