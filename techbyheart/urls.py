from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path, include

from rest_framework import status
from django.contrib import admin

@api_view(['GET'])
def api_over_view(request):
    api_urls = [
        {
            'Default admin panel': '/admin/',
        },
        {
            'Costumer':"",
            'Login': '/api/v1/login/',
            'Refresh': '/api/v1/token/refresh/',
            'Register': '/api/v1/register/',
            'List products': '/api/v1/products/',
            'List categories': '/api/v1/categories/',
            'List subcategories': '/api/v1/subcategories/',
            'List cart': '/api/v1/add/to/cart/<user_id>/',
            'Add to cart': '/api/v1/add/to/cart/<user_id>/',
        },
        {
            'Store admin':"",
            'Login': '/api/v1/storeadmin/login/',
            'Register': '/api/v1/storeadmin/register/',
            'Add product': '/api/v1/storeadmin/add/product/',
        },
        {
            'Super admin':"",
            'Login': '/api/v1/superadmin/login/',
            'Register': '/api/v1/superadmin/register/',
        }

        # 'List procuct': '/api/v1/list/product/',
        # 'Order': '/api/v1/order/',
        # 'Payment transaction': '/api/v1/payment/transaction/',

        # 'List users': '/api/v1/admin/users/',
        # 'Analytics': '/api/v1/admin/analytics/',
        # 'Ledger': '/api/v1/admin/ledger/',
    ]
    return  Response(api_urls, status=status.HTTP_201_CREATED)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_over_view, name="api_over_view"),
    path('api/v1/superadmin/', include('superadmin.urls')),
    path('api/v1/storeadmin/', include('storeadmin.urls')),
    path('api/v1/', include('customer.urls')),
]
