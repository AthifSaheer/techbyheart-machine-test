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
    Post method format.
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
        Post method format.
        {
            "product": <product_id>,
            "store": <product_id>
        }
        """
        product = request.data['product']
        store = request.data['store']

        try:
            prd_qr = Product.objects.get(id=product)
            store_qr = Store.objects.get(id=store)
        except:
            data = {"error": "Something went wrong!"}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        try:
            str_prd = StoreProduct.objects.get(product=prd_qr, store=store_qr)
        except StoreProduct.DoesNotExist:
            data = {"error": "Product({}) does not exist in this store({})!".format(prd_qr, store_qr)}
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        if str_prd.stock < 1:
            data = {"error": "Product out of stock!"}
            return Response(data, status=status.HTTP_403_FORBIDDEN)
        else:
            if Cart.objects.filter(user=id, product=product, store=store):
                cart = Cart.objects.get(user=id, product=product, store=store)

                if cart.quantity == str_prd.stock:
                    data = {"error": "Product stock maximum exceed!"}
                    return Response(data, status=status.HTTP_403_FORBIDDEN)

                cart.quantity += 1
                cart.save()
            else:
                cart_qr = Cart.objects.filter(user=id).first()
                print("=============================cart---------", cart_qr)
                if cart_qr == None or cart_qr.store == store_qr:
                    cart = Cart()
                    cart.user = User.objects.get(id=id)
                    cart.product = prd_qr
                    cart.store = store_qr
                    cart.save()
                else:
                    data = {"error": "You can't purchase multiple products from multiple stores!"}
                    return Response(data, status=status.HTTP_403_FORBIDDEN)

        srzl = CartSerializer(cart)
        return Response(srzl.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def checkout(request):
    """
    Post method format.
    {
        "username" : "username",
        "password" : "xzaq1234"
    }
    """
    if request.method == 'POST':
        user = request.data['user']
        cart = Cart.objects.filter(user=user)
        for cr in cart:
            order = Order()
            order.user = cr.user
            order.product = cr.product
            order.store = cr.store
            order.quantity = cr.quantity
            order.save()
        cart.delete()
        data = {"suceess": "success"}
        return Response(data, status=status.HTTP_201_CREATED)
    data = {"error": "Something went wrong!"}
    return Response(data, status=status.HTTP_403_FORBIDDEN)
    
@api_view(['GET'])
def orders(request, id):
    try:
        orders = Order.objects.filter(user=id)
        srzl = OrderSerializer(orders, many=True)
        return Response(srzl.data, status=status.HTTP_201_CREATED)
    except:
        data = {"error": "Something went wrong!"}
        return Response(data, status=status.HTTP_403_FORBIDDEN)