from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.storeadmin_login, name='storeadmin_login'),
    path('register/', views.storeadmin_register, name='storeadmin_register'),
]
