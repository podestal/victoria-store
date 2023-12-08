from rest_framework_nested import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('products', views.ProdcutViewSet, basename='products')
router.register('brands', views.BrandViewSet, basename='brands')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('images', views.ProductImageViewSet, basename='product-images')

urlpatterns = router.urls + products_router.urls
