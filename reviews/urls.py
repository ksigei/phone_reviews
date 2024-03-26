from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('products/<int:pk>/review/', views.review_create, name='review_create'),
    path('products/<int:pk>/rate/', views.rate_product, name='rate_product'),
]
