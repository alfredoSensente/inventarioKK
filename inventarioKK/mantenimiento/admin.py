from django.contrib import admin
from .models import Mantenimiento
from .models import TipoCorrectivo
from .models import Correctivo
from .models import MetodoPreventivo
from .models import TipoPreventivo
from .models import Preventivo
from .models import Innovativo

# Register your models here.
admin.site.register(Mantenimiento)
admin.site.register(TipoCorrectivo)
admin.site.register(Correctivo)
admin.site.register(MetodoPreventivo)
admin.site.register(TipoPreventivo)
admin.site.register(Preventivo)
admin.site.register(Innovativo)
