from django.shortcuts import render
from .models import Equipo, Edificio
from django.views import generic, View
from .forms import EquipoForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from .utils import render_to_pdf

# Create your views here.
class ListaDeEquipos(generic.ListView):
    """vista generica tabla equipos"""
    paginate_by = 7
    template_name= 'equipo/index.html'
    context_object_name = 'lista_equipo'
    model = Equipo
   
class EquipoCreate(generic.CreateView):
    """Crear un nuevo equipo"""
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/nuevo_equipo.html'
    success_url = reverse_lazy('equipo:lista_de_equipos')

class DescripcionEquipo(generic.DetailView):
    """Muestra una descripcion de cada Equipo"""
    template_name = 'equipo/descripcion_equipo.html'
    context_object_name = 'descripcion_equipo'
    model = Equipo

class EquipoUpdate(generic.UpdateView):
    """Actualiza el registro de un equipo"""
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/nuevo_equipo.html'
    success_url = reverse_lazy('equipo:lista_de_equipos')

class BusquedaEquipo(generic.ListView):
    """Busca un Equipo"""
    model = Equipo
    context_object_name = 'busqueda_equipo'
    template_name = 'equipo/busqueda_equipo.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Equipo.objects.filter(
           Q(id_equipo__icontains=query) | Q(id_tipo_equipo__nombre_tipo_equipo__icontains=query) | Q(id_marca__nombre_marca__icontains=query)| 
           Q(id_estado_equipo__nombre_estado_equipo__icontains=query) | Q(descripcion__icontains=query) | Q(id_ubicacion__nombre_ubicacion__icontains=query) | Q(id_ubicacion__id_edificio__nombre_edificio__icontains=query) 
        )
        return object_list

def PDF(request, id_equipo):
    """Muestra al Equipo seleccionado en un PDF y las opciones de Guardar dicho PDF y/o Imprimirlo"""
    descripcion_equipo = Equipo.objects.get(pk=id_equipo)
    data = {
            'descripcion_equipo': descripcion_equipo
        }
    pdf = render_to_pdf('equipo/lista.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

