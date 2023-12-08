from rest_framework import serializers
from storeapi import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['title', 'unit_price', 'category']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ['id', 'image']

    def save(self, **kwargs):
        product_id = self.context['product_id']
        self.instance = models.ProductImage.objects.create(product_id = product_id, **self.validated_data)
        return self.instance
    
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = '__all__'
    
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    category = CategorySerializer()
    brand = BrandSerializer()
    class Meta:
        model = models.Product
        fields = ['id', 'title', 'unit_price', 'category', 'brand', 'images']