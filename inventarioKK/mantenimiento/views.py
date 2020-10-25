"""Vistas de Mantenimiento"""
from django.views import generic
from django.urls import reverse_lazy
from datetime import datetime
from datetime import date
from equipo.utils import render_to_pdf
from django.http import HttpResponse
from .models import Mantenimiento
from .forms import MantenimientoForm

# Create your views here.
class Index(generic.ListView):
    """Vista generica Index"""
    # Matenimiento.objects.all()
    template_name = 'mantenimiento/index.html'
    context_object_name = 'tabla_mantenimiento'
    model = Mantenimiento

class DescripcionMatenimiento(generic.DetailView):
    """Vista generica de los matenimientos realizados a un equipo"""
    # Mantenimiento.objects.get(pk=1)
    model = Mantenimiento
    template_name = 'mantenimiento/descripcion.html'
    context_object_name = 'descripcion_mantenimiento'

class MantenimientoUpdate(generic.UpdateView):
    """Actualiza el registro de un equipo"""
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/nuevo_mantenimiento.html'
    success_url = reverse_lazy('mantenimiento:index')

class MantenimientoCreate(generic.CreateView):
    """Vista para agregar un registro de mantenimiento"""
    model = Mantenimiento
    form_class = MantenimientoForm
    context_object_name = 'mantenimiento_objeto'
    template_name = 'mantenimiento/nuevo_mantenimiento.html'
    success_url = reverse_lazy('mantenimiento:index')

def PDF(request, id_mantenimiento):
    """Muestra al Equipo seleccionado en un PDF y las opciones de Guardar dicho PDF y/o Imprimirlo"""
    descripcion_mantenimiento = Mantenimiento.objects.get(pk=id_mantenimiento)
    hora = datetime.now()
    """format = hora.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M')"""
    data = {
            'descripcion_equipo': descripcion_mantenimiento,
            'fechaHora' : hora,
            
        }
    pdf = render_to_pdf('equipo/lista.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def generador(request):
    """
    Termina de generar codigo
    """
    if request.method == 'POST':
        print('llego')
        if 'letras' in request.POST:
            letras = request.POST['letras'].upper()
            numero = str(Mantenimiento.objects.filter(id_mantenimiento__startswith=letras).count()+1).zfill(3)
            anio = str(date.today().year)
            codigo = letras+anio[:2]+numero
            print(codigo)
            return HttpResponse(codigo)
    return HttpResponse('FAIL!!!!!')
