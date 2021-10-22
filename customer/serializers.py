from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

# THIS CLASSES WILL BE SERIALIZER THE MODELS
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
