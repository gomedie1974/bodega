from django.shortcuts import render

# Create your views here.

def listar_empleados(request):
    contexto = {
        "jefe": "Pedro",
        "empleados": [
            {'nombre': 'Diego', 'apellido': 'Gomez'},
            {'nombre': 'Tomas', 'apellido': 'Duarte'},
            {'nombre': 'Lio', 'apellido': 'Me10'},
        ]
    }
    http_response = render(
        request=request,
        template_name='lista_empleados.html',
        context=contexto,
    )
    return http_response

