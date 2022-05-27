from django.contrib import admin
from django.urls import path
from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list_products',
        'post': 'create_product'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve_product',
        'put': 'update_product',
        'delete': 'destroy_product',
    })),
    path('user', UserAPIView.as_view()),
]
