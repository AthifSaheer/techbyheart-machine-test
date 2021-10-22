# from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from .serializers import *
from .models import *

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

@api_view(['GET'])
def products(request):
    try:
        prdcts = Product.objects.all()
        srzl = ProductSerializer(prdcts, context={"request": request}, many=True)
        return Response(srzl.data, status=status.HTTP_201_CREATED)
    except Product.DoesNotExist:
        data = {"error": "Something went wrong!"}
        return Response(data, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def categories(request):
    try:
        ctgrs = Category.objects.all()
        srzl = CategorySerializer(ctgrs, context={"request": request}, many=True)
        return Response(srzl.data, status=status.HTTP_201_CREATED)
    except Category.DoesNotExist:
        data = {"error": "Something went wrong!"}
        return Response(data, status=status.HTTP_403_FORBIDDEN)
        
@api_view(['GET'])
def subcategories(request):
    try:
        sub_ctgrs = SubCategory.objects.all()
        srzl = SubCategorySerializer(sub_ctgrs, context={"request": request}, many=True)
        return Response(srzl.data, status=status.HTTP_201_CREATED)
    except SubCategory.DoesNotExist:
        data = {"error": "Something went wrong!"}
        return Response(data, status=status.HTTP_403_FORBIDDEN)
        
# @login_required(login_url='login')
@api_view(['POST', 'GET'])
def add_to_cart(request, id):
    if request.method == 'GET':
        try:
            cart = Cart.objects.filter(user=id)
            srzl = CartSerializer(cart, context={'request': request}, many=True)
            return Response(srzl.data, status=status.HTTP_201_CREATED)
        except Cart.DoesNotExist:
            data = {"error": "Something went wrong!"}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'POST':
        """
        {
            "product": 1
        }
        """
        product = request.data['product']

        if Cart.objects.filter(user=id, product=product):
            cart = Cart.objects.get(user=id, product=product)
            cart.quantity += 1
            cart.save()
        else:
            cart = Cart()
            cart.user = User.objects.get(id=id)
            cart.product = Product.objects.get(id=product)
            cart.save()

        srzl = CartSerializer(cart)
        return Response(srzl.data, status=status.HTTP_201_CREATED)

