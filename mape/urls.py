"""mape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.inicio, name='inicio')
Class-based views
    1. Add an import:  from other_app.views import inicio
    2. Add a URL to urlpatterns:  path('', inicio.as_view(), name='inicio')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
 
from WebApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')),
    path('tienda/', include('tienda.urls')),
    path('contacto/', include('contacto.urls')),
    path('carro/', include('carro.urls')),
    path('', include('WebApp.urls')),
]
