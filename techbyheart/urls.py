from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superadmin/', include('superadmin.urls')),
    path('storeadmin/', include('storeadmin.urls')),
    path('', include('customer.urls')),
]
