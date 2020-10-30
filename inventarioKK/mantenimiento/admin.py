"""Modelos de mantenimiento editables en admin"""
from django.contrib import admin
from .models import Mantenimiento
from .models import TipoMantenimiento
from .models import Bodega
from .models import TipoRecurso
from .models import MantenimientoPorBodega


# Register your models here.
admin.site.register(Mantenimiento)
admin.site.register(TipoMantenimiento)
admin.site.register(Bodega)
admin.site.register(TipoRecurso)
admin.site.register(MantenimientoPorBodega)


