from django.urls import path
from .views import VRegistro, CerrarSesion, Logear

urlpatterns = [
    path('', VRegistro.as_view(), name="Registros"),
    path('CerrarSesion',CerrarSesion, name="Cerrar_sesion"),
    path('logear', Logear, name="logear"),

]