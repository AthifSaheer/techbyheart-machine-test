from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from .serializers import *
from .models import *

@api_view(['GET'])
def api_over_view(request):
    api_urls = {
        'Default admin panel': '/admin/',
        
        'Costumer':"",
        'Login': '/api/v1/login/',
        'Refresh': '/api/v1/token/refresh/',
        'Register': '/api/v1/register/',

        'Store admin':"",

        'Super admin':"",

        'List procuct': '/api/v1/list/product/',
        'Order': '/api/v1/order/',
        'Payment transaction': '/api/v1/payment/transaction/',

        'List users': '/api/v1/admin/users/',
        'Analytics': '/api/v1/admin/analytics/',
        'Ledger': '/api/v1/admin/ledger/',
    }
    return  Response(api_urls, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def register(request):
    """
    {
        "username" : "athif",
        "email" : "athif@gmail.com",
        "password" : "xzaq1234"
    }
    """
    if request.method == 'POST':
        srzl = UserRegisterSerializer(data=request.data)
        
        if not srzl.is_valid():
            data = {'error': 'Something went wrong!'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        srzl.save()

        user = User.objects.get(username=srzl.data['username'])
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_201_CREATED)

