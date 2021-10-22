from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path, include

from rest_framework import status
from django.contrib import admin

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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_over_view, name="api_over_view"),
    path('api/v1/superadmin/', include('superadmin.urls')),
    path('api/v1/storeadmin/', include('storeadmin.urls')),
    path('api/v1/', include('customer.urls')),
]
