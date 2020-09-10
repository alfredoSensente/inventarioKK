from django.shortcuts import render, get_object_or_404
from .models import Mantenimiento

# Create your views here.
def index(request):
    """Muestra un listado de los mantenimientos existentes"""
    listado_mantenimiento = Mantenimiento.objects.all()
    context = {
        'listado_mantenimiento' : listado_mantenimiento,
    }
    return render(request, 'mantenimiento/index.html', context)

def descripcion(request, id_mantenimiento):
    """Muestra una descripcion del mantenimiento realizado a cierto equipo"""
    descripcion_mantenimiento = get_object_or_404(Mantenimiento, pk=id_mantenimiento)
    context = {
        'descripcion_mantenimiento' : descripcion_mantenimiento
    }
    return render(request, 'mantenimiento/descripcion.html', context)
