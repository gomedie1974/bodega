from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from control_empleados.forms import BodegaFormulario
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


""" def cargar_bodega(request):
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
    ) """

def cargar_bodega(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = BodegaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            codigo = data["codigo"]
            # creo un curso en memoria RAM
            bodega = Bodega(nombre=nombre, codigo=codigo)
            # Lo guardan en la Base de datos
            bodega.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('listar_bodegas')  
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = BodegaFormulario()
    http_response = render(
        request=request,
        template_name='control_empleados/formulario_alta_bodegas.html',
        context={'formulario': formulario}
    )
    return http_response



def buscar_bodegas(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        #bodegas = Bodega.objects.filter(codigo__contains=busqueda)
        # Ejemplo filtro avanzado
        bodegas = Bodega.objects.filter(
            Q(nombre__icontains=busqueda) | Q(codigo__contains=busqueda)
        )

        contexto = {
            "bodegas": bodegas,
        }
        http_response = render(
            request=request,
            template_name='control_empleados/listar_bodegas.html',
            context=contexto,
        )
        return http_response
