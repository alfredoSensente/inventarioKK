from django.contrib import admin
from .models import Marca
from .models import TipoEquipo
from .models import Edificio
from .models import Ubicacion
from .models import EstadoEquipo
from .models import Equipo


# Register your models here.

admin.site.register(Marca)
admin.site.register(TipoEquipo)
admin.site.register(Edificio)
admin.site.register(Ubicacion)
admin.site.register(EstadoEquipo)
admin.site.register(Equipo)

