"""Vistas de la Aplicacion Empleado"""

from django.urls import reverse_lazy
"""Vistas de la App Empleado"""
from django.views import generic
from .models import Empleado
from .forms import EmpleadoForm


# Create your views here.
class Indice(generic.ListView):
    """Vista Genèrica de Tabla de Empleados"""
    template_name = 'empleado/e_index.html'
    context_object_name = 'lista_empleado'
    model = Empleado

class DescripcionEmpleado(generic.DetailView):
    """Muestra una descripcion de cada Empleado"""
    template_name = 'empleado/descripcion_e.html'
    context_object_name = 'descripcion_empleado'
    model = Empleado

class CrearEmpleado(generic.CreateView):
    """Muestra el formulario para crear un nuevo Empleado"""
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/nuevo_empleado.html'
    success_url = reverse_lazy('empleado:mensaje_empleado')

