"""Vistas de Mantenimiento"""
from django.views import generic
from django.urls import reverse_lazy
from .forms import CorrectivoForm
from .models import Mantenimiento, Correctivo

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

class CorretivoCreate(generic.CreateView):
    """Formulario para agregar un nuevo mantenimiento correctivo"""
    model = Correctivo
    form_class = CorrectivoForm
    template_name = 'mantenimiento/nuevo_correctivo.html'
    success_url = reverse_lazy('mantenimiento:index')

class MantenimientoDelete(generic.DeleteView):
    """Vista para eleminar un registro de mantenimiento"""
    model = Mantenimiento
    context_object_name = 'mantenimiento_objeto'
    template_name = 'mantenimiento/borrar_mantenimiento.html'
    success_url = reverse_lazy('mantenimiento:index')
