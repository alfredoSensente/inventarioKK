from django.contrib import admin
from .models import Cargo
from .models import Sexo
from .models import EstadoEmpleado
from .models import Empleado
from .models import EmpleadoPorMantenimiento

# Register your models here.
admin.site.register(Cargo)
admin.site.register(Sexo)
admin.site.register(EstadoEmpleado)
admin.site.register(Empleado)
admin.site.register(EmpleadoPorMantenimiento)