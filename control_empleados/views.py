from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from control_empleados.models import Empleado


# Create your views here.

def listar_empleados(request):
    contexto = {
        "jefe": "Lionel",
        "empleados": [
            {'nombre': 'Diego', 'apellido': 'Gomez'},
            {'nombre': 'Tomas', 'apellido': 'Duarte'},
            {'nombre': 'Lio', 'apellido': 'Me10'},
        ]
    }
    http_response = render(
        request=request,
        template_name='control_empleados/lista_empleados.html',
        context=contexto,
    )
    return http_response

