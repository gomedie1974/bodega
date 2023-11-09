from django.db import models

# Create your models here.
class Bodega(models.Model):
    # los atributos de clase (son las columnas de la tabla)
    nombre = models.CharField(max_length=64)
    codigo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Empleado(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Jefe(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(blank=True, null=True)
    
class Vinos(models.Model):
    Bodega = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    cepa = models.CharField(max_length=256)
    uva = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

class Premio(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    tiene_premio = models.BooleanField(default=False) 