from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, auth
from rest_framework import status
from .serializers import *

@api_view(['POST'])
def storeadmin_login(request):
    """
    {
        "username" : "shakkir",
        "password" : "xzaq1234"
    }
    """
    if request.method == 'POST':
        user = request.data['username']
        password = request.data['password']
        auth_user = auth.authenticate(username=user, password=password)
        if auth_user is not None:
            usr = User.objects.get(username=user)
            if usr.is_superuser == True:
                srzl = StoreAdminLoginSerializer(usr)
               
                refresh = RefreshToken.for_user(usr)
                data = {
                    'refresh' : str(refresh),
                    'access' : str(refresh.access_token),
                }
                
                return Response(data, status=200)
            else:
                return Response({"error": "Invalid username or password!"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"error": "Invalid username or password!"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def storeadmin_register(request):
    """
    {
        "username" : "shakkir",
        "email" : "shakkir@gmail.com",
        "password" : "xzaq1234"
    }
    """
    if request.method == 'POST':
        srzl = StoreAdminRegisterSerializer(data=request.data)
        
        if not srzl.is_valid():
            data = {'error': 'Something went wrong!'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        srzl.save()

        user = User.objects.get(username=srzl.data['username'])
        user.is_superuser = True
        user.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_201_CREATED)
