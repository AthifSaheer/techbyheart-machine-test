from django.contrib import admin
from .models import *

admin.site.register([Store, Category, SubCategory, Product, StoreProduct])