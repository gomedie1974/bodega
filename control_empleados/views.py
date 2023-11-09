from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from control_empleados.models import Empleado, Bodega

# Create your views here.

def listar_empleados(request):
    contexto = {
        "jefe": "Lionel",
        "empleados": Empleado.objects.all 
    }
    http_response = render(
        request=request,
        template_name='control_empleados/lista_empleados.html',
        context=contexto,
    )
    return http_response

def listar_bodegas(request):
    contexto = {
         "bodegas": Bodega.objects.all 
    }
    http_response = render(
        request=request,
        template_name='control_empleados/listar_bodegas.html',
        context=contexto,
    )
    return http_response


def cargar_bodega(request):
    if request.method == "POST":
        # GUARDA LOS DATOS
        data = request.POST

        # GUARDO LA BODEGA EN LA RAM
        bodega = Bodega(nombre=data['nombre'], codigo=data['codigo'])

        # GUARDO LA BODEGA EN LA BASE DE DATOS
        bodega.save()
        url_exitosa = reverse('listar_bodegas')
        return redirect(url_exitosa)
    else: # GET
        # CARGA FORMULARIO INICIAL
        return render(
        request=request,
        template_name='control_empleados/formulario_alta_bodegas.html',
    )

