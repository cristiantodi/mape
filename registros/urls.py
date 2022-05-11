from django.urls import path
from .views import VRegistro, CerrarSesion

urlpatterns = [
    path('', VRegistro.as_view(), name="Registros"),
    path('CerrarSesion',CerrarSesion, name="Cerrar_sesion"),

]