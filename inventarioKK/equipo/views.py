from django.shortcuts import render
from .models import Equipo

# Create your views here.
def lista_de_equipos(request):
    """contexto para la tabla equipo"""
    lista_equipo = Equipo.objects.all()
    context = {'lista_equipo': lista_equipo}
    return render(request, 'equipo/index.html', context)
