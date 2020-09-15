from django.shortcuts import render
from .models import Equipo
from django.views import generic
from .forms import EquipoForm
from django.urls import reverse_lazy

# Create your views here.
class ListaDeEquipos(generic.ListView):
    """vista generica tabla equipos"""
    template_name= 'equipo/index.html'
    context_object_name = 'lista_equipo'
    model = Equipo
   
class EquipoCreate(generic.CreateView):
    """Crear un nuevo paciente"""
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/nuevo_equipo.html'
    success_url = reverse_lazy('equipo:lista_de_equipos')

