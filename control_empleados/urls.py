from django.urls import path
from control_empleados.views import (listar_empleados, cargar_bodega, listar_bodegas,
buscar_bodegas
)

urlpatterns = [
    path('empleados/', listar_empleados, name='lista_empleados'),
    path('alta-bodegas/', cargar_bodega, name='cargar_bodega'),
    path('lista-bodegas/', listar_bodegas, name='listar_bodegas'),
    path('buscar-bodegas/', buscar_bodegas, name='buscar_bodegas'),


    
]
