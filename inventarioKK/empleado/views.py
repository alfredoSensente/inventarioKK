"""Vistas de la Aplicacion Empleado"""
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Empleado
from .forms import EmpleadoForm
from django.shortcuts import render

# Create your views here.
class Indice(generic.ListView):
    """Vista Genèrica de Tabla de Empleados"""
    template_name = 'empleado/e_index.html'
    context_object_name = 'lista_empleado'
    model = Empleado
    paginate_by = 5

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

class EditarEmpleado(generic.UpdateView):
    """Actualiza el registro de un Empleado"""
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/nuevo_empleado.html'
    success_url = reverse_lazy('empleado:mensaje_empleado')

class EliminarEmpleado(generic.DeleteView):
    """Elimina un Empleado"""
    model = Empleado
    context_object_name = 'descripcion_empleado'
    template_name = 'empleado/eliminar_empleado.html'
    success_url = reverse_lazy('empleado:mensaje_empleado')

class BusquedaEmpleado(generic.ListView):
    """Busca un Empleado"""
    model = Empleado
    context_object_name = 'eliminacion_empleado'
    template_name = 'empleado/busqueda_empleado.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Empleado.objects.filter(
           Q(id_empleado__icontains=query) | Q(nombre__icontains=query) | Q(apellido__icontains=query)| 
           Q(dui__icontains=query) | Q(nit__icontains=query) | Q(fecha_nacimiento__icontains=query)| 
           Q(telefono_fijo__icontains=query) | Q(id_ubicacion__nombre_ubicacion__icontains=query) |
           Q(id_ubicacion__id_edificio__nombre_edificio__icontains=query)
        )
        return object_list

def ErrorEmpleado(request):
    return render(request, 'empleado/error.html')



        
        


    

