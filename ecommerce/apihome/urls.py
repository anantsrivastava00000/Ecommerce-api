from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    # path('product_variant/', views.product_variants.as_view()),
    path('product_variant/', views.product_variant),
    # path('product/', views.product.as_view()),
    # path('product/', views.product),
    
    # path('loginapi/', views.loginapi),
] 

