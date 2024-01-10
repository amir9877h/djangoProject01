from django.urls import path
from catalogue.views import products_list, products_detail,category_products

urlpatterns = [
    path('products/list/', products_list, name='product-list'),
    path('products/detail/<int:pk>', products_detail, name='product-detail'),
    path('category/<int:pk>/products', category_products, name='category_products'),
]
