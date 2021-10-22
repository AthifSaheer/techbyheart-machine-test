from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register, name="register"),

    path('products/', views.products, name="products"),
    path('categories/', views.categories, name="categories"),
    path('subcategories/', views.subcategories, name="subcategories"),
    path('add/to/cart/<int:id>/', views.add_to_cart, name="add_to_cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('orders/<int:id>/', views.orders, name="orders"),
]
