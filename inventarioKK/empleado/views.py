from django.shortcuts import render, get_object_or_404
from .models import Empleado

# Create your views here.
def mensaje_empleado(request):
    """Muestra la template de Mensaje Empleado"""
    latest_empleado_list = Empleado.objects.all()
    context = {'latest_empleado_list': latest_empleado_list}
    return render(request, 'empleado/e_index.html', context)

def descripcion_empleado(request, id_empleado):
    """Muestra la descripcion de un Empleado"""
    descripcion_empleado = get_object_or_404(Empleado, pk=id_empleado)
    context = {'descripcion_empleado': descripcion_empleado}
    return render(request, 'empleado/descripcion_e.html', context)