from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.superadmin_login, name='superadmin_login'),
    path('register/', views.superadmin_register, name='superadmin_register'),
]
