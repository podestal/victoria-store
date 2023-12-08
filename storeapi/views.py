from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from storeapi import models
from storeapi import serializers

class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class BrandViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.BrandSerializer

class ProdcutViewSet(ModelViewSet):
    queryset = models.Product.objects.select_related('category').prefetch_related('images').all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateProductSerializer
        return serializers.ProductSerializer
    
class ProductImageViewSet(ModelViewSet):
    serializer_class = serializers.ProductImageSerializer

    def get_queryset(self):
        return models.ProductImage.objects.filter(product_id = self.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
