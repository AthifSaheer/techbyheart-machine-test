from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from superadmin.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'phone_number']

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    store = StoreSerializer()
    product = ProductSerializer()
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    store = StoreSerializer()
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = '__all__'
