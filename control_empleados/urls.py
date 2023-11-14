from django.urls import path
from control_empleados.views import (listar_empleados, cargar_bodega, listar_bodegas,
buscar_bodegas, cargar_empleado, buscar_empleados, eliminar_empleado, eliminar_bodega,
editar_empleado
)

urlpatterns = [
    path('empleados/', listar_empleados, name='lista_empleados'),
    path('alta-empleados/', cargar_empleado, name='cargar_empleado'),
    path('buscar-empleados/', buscar_empleados, name='buscar_empleados'),
    #<int:id> es el identificador del empleado a borrar
    path('eliminar-empleados/<int:id>', eliminar_empleado, name='eliminar_empleado'), 
    path('editar_empleado/<int:id>', editar_empleado, name='editar_empleado'),

    path('alta-bodegas/', cargar_bodega, name='cargar_bodega'),
    path('lista-bodegas/', listar_bodegas, name='listar_bodegas'),
    path('buscar-bodegas/', buscar_bodegas, name='buscar_bodegas'),
    path('eliminar_bodega/<int:id>', eliminar_bodega, name='eliminar_bodega'),

 
    
]
