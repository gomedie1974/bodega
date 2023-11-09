from django.contrib import admin

# Register your models here.
from control_empleados.models import Empleado, Bodega, Jefe, Premio

admin.site.register(Empleado)
admin.site.register(Bodega)
admin.site.register(Jefe)
admin.site.register(Premio)