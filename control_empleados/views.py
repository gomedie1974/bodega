from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from control_empleados.forms import BodegaFormulario, EmpleadoFormulario
from control_empleados.models import Empleado, Bodega


# Create your views here.

def listar_empleados(request):
    contexto = {
        "jefe": "Lionel",
        #obtiene todos los datos de la base de tados Empleado
        "empleados": Empleado.objects.all 
    }
    http_response = render(
        request=request,
        template_name='control_empleados/lista_empleados.html',
        context=contexto,
    )
    return http_response

def buscar_empleados(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        #bodegas = Bodega.objects.filter(codigo__contains=busqueda)
        # Ejemplo filtro avanzado
        empleados = Empleado.objects.filter(
            Q(nombre__icontains=busqueda) | Q(apellido__contains=busqueda)
        )

        contexto = {
            "empleados": empleados,
        }
        http_response = render(
            request=request,
            template_name='control_empleados/lista_empleados.html',
            context=contexto,
        )
        return http_response

def cargar_empleado(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = EmpleadoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            apellido = data["apellido"]
            email = data["email"]
            telefono = data["telefono"]
            dni = data["dni"]
            fecha_nacimiento = data["fecha_nacimiento"]

            # creo un curso en memoria RAM
            empleados = Empleado(nombre=nombre, apellido=apellido, email=email, telefono=telefono, dni=dni, fecha_nacimiento=fecha_nacimiento)
            # Lo guardan en la Base de datos
            empleados.save()

            # Redirecciono al usuario a la lista de
            url_exitosa = reverse('lista_empleados')  
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = EmpleadoFormulario()
    http_response = render(
        request=request,
        template_name='control_empleados/formulario_alta_empleado.html',
        context={'formulario': formulario}
    )
    return http_response

def editar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    if request.method == "POST":
        formulario = EmpleadoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            empleado.nombre = data["nombre"]
            empleado.apellido = data["apellido"]
            empleado.email = data["email"]
            empleado.telefono = data["telefono"]
            empleado.dni = data["dni"]
            empleado.fecha_nacimiento = data["fecha_nacimiento"]
            empleado.save()

            url_exitosa = reverse('lista_empleados')  
            return redirect(url_exitosa)
        
    
    else:  # GET
        inicial = {
            'nombre' : empleado.nombre,
            'apellido' : empleado.apellido,
            'email' : empleado.email,
            'telefono' : empleado.telefono,
            'dni' : empleado.dni,
            'fecha_nacimiento' : empleado.fecha_nacimiento,
        }
        formulario = EmpleadoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_empleados/formulario_alta_empleado.html',
        context={'formulario': formulario},
    )
  
def eliminar_empleado(request, id):
    #obtengo el empleados de la BD
    empleado = Empleado.objects.get(id=id)
    if request.method == 'POST':
        #borra el empleado de la BD
        empleado.delete()
        #redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_empleados')
        return redirect(url_exitosa)

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

def eliminar_bodega(request, id):
    bodega = Bodega.objects.get(id=id)
    if request.method == 'POST':
        bodega.delete()
        #redireccionamos a la URL exitosa
        url_exitosa = reverse('listar_bodegas')
        return redirect(url_exitosa)
        
def editar_bodega(request, id):
    bodega = Bodega.objects.get(id=id)
    if request.method == "POST":
        formulario = BodegaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            bodega.nombre = data["nombre"]
            bodega.codigo = data["codigo"]
            bodega.save()

            url_exitosa = reverse('listar_bodegas')  
            return redirect(url_exitosa)
        
    
    else:  # GET
        inicial = {
            'nombre' : bodega.nombre,
            'codigo' : bodega.codigo,
        }
        formulario = BodegaFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_empleados/formulario_alta_bodegas.html',
        context={'formulario': formulario},
    )


# VISTAS BASADAS EN CLASES 
#EMPLEADOS
class EmpleadoListView(ListView):
    model = Empleado
    template_name='control_empleados/lista_empleados.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    fields = ('apellido', 'nombre', 'email', 'telefono', 'dni', 'fecha_nacimiento')
    success_url = reverse_lazy('lista_empleados')
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    success_url = reverse_lazy('lista_empleados')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = ('apellido', 'nombre', 'email', 'telefono', 'dni', 'fecha_nacimiento')
    success_url = reverse_lazy('lista_empleados')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('lista_empleados')


#BODEGAS
class BodegaListView(ListView):
    model = Bodega
    template_name='control_empleados/listar_bodegas.html'

class BodegaCreateView(CreateView):
    model = Bodega
    fields = ('nombre', 'codigo')
    success_url = reverse_lazy('listar_bodegas')
    
class BodegaDetailView(DetailView):
    model = Bodega
    success_url = reverse_lazy('listar_bodegas')

class BodegaUpdateView(UpdateView):
    model = Bodega
    fields = ('nombre', 'codigo')
    success_url = reverse_lazy('listar_bodegas')

class BodegaDeleteView(DeleteView):
    model = Bodega
    success_url = reverse_lazy('listar_bodegas')
