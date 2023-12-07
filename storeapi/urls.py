from rest_framework_nested import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProdcutViewSet, basename='products')

urlpatterns = router.urls

# urlpatterns = [
        # path('products/', views.vic),
#     path('products/', views.ProductList.as_view()), 
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path('collections/<int:pk>/', views.CollectionDetail.as_view()),
# ]