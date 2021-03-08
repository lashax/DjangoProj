from rest_framework import serializers

from .models import Product, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'origin_country', 'origin_date']


class ProductSerializer(serializers.ModelSerializer):
    designer = serializers.ReadOnlyField(source='designer.username')

    class Meta:
        model = Product
        fields = ['id', 'brand', 'title', 'description', 'price', 'designer']
