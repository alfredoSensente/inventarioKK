"""Vistas de Mantenimiento"""
from django.views import generic
from django.urls import reverse_lazy
from .models import Mantenimiento

# Create your views here.
class Index(generic.ListView):
    """Vista generica Index"""
    # Matenimiento.objects.all()
    template_name = 'mantenimiento/index.html'
    context_object_name = 'listado_mantenimiento'
    model = Mantenimiento

class DescripcionMatenimiento(generic.DetailView):
    """Vista generica de los matenimientos realizados a un equipo"""
    # Mantenimiento.objects.get(pk=1)
    model = Mantenimiento
    template_name = 'mantenimiento/descripcion.html'
    context_object_name = 'descripcion_mantenimiento'

class MantenimientoDelete(generic.DeleteView):
    """Vista para eleminar un registro de mantenimiento"""
    model = Mantenimiento
    context_object_name = 'mantenimiento_objeto'
    template_name = 'mantenimiento/borrar_mantenimiento.html'
    success_url = reverse_lazy('mantenimiento:index')
