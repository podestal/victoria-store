from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from storeapi import models
from storeapi import serializers

class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class ProdcutViewSet(ModelViewSet):
    queryset = models.Product.objects.select_related('category').all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateProductSerializer
        return serializers.ProductSerializer
