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
    context_object_name = 'contexto'
    template_name = 'mantenimiento/nuevo_correctivo.html'
    success_url = reverse_lazy('mantenimiento:index')

    def get_context_data(self, **kwargs):
        
        # Call class's get_context_data method to retrieve context
        context = super().get_context_data(**kwargs)
        if Correctivo.objects.count != 0:
            contexto = 'CO-' + str(Correctivo.objects.count()+1).zfill(4)
        elif Correctivo.objects.count < 0:
            contexto = 'El codigo de registro no puede ser negativo'
        else:
            contexto = 'CO-' + '0'.zfill(4) 
        context['page_title'] = contexto
        return context

class MantenimientoDelete(generic.DeleteView):
    """Vista para eleminar un registro de mantenimiento"""
    model = Mantenimiento
    context_object_name = 'mantenimiento_objeto'
    template_name = 'mantenimiento/borrar_mantenimiento.html'
    success_url = reverse_lazy('mantenimiento:index')
