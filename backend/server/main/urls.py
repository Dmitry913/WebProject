from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('api/', include('app.urls'))
]
