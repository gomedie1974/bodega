from django import forms


class BodegaFormulario (forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    codigo = forms.IntegerField(required=True, max_value=100000)
class EmpleadoFormulario (forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)   
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=True, max_length=64)
    dni = forms.CharField(required=True, max_length=32)
    fecha_nacimiento = forms.DateField(required=True)