from django.urls import path
from AppMantenimiento.views import *

urlpatterns = [
    path("nuevo_mecanico/", agregar_mecanico),
    path("nuevo_vehiculo/", agregar_vehiculo),
    path("nuevo_mantenimiento/", agregar_mantenimiento),
    path("buscar_mecanico/", buscar_mecanico),
    path("resultado/", mostrar_mecanico),
]