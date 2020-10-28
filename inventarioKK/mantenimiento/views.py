"""Vistas de Mantenimiento"""
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from datetime import datetime
from datetime import date
from equipo.utils import render_to_pdf
from django.http import HttpResponse, HttpResponseRedirect
from .models import Mantenimiento, Empleado, Equipo, TipoMantenimiento, Bodega
from .forms import MantenimientoForm, BodegaForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Index(LoginRequiredMixin, generic.ListView):
    """Vista generica Index"""
    # Matenimiento.objects.all()
    paginate_by = 5
    template_name = 'mantenimiento/index.html'
    context_object_name = 'tabla_mantenimiento'
    model = Mantenimiento

class DescripcionMatenimiento(LoginRequiredMixin, generic.DetailView):
    """Vista generica de los matenimientos realizados a un equipo"""
    # Mantenimiento.objects.get(pk=1)
    model = Mantenimiento
    template_name = 'mantenimiento/descripcion.html'
    context_object_name = 'descripcion_mantenimiento'

class MantenimientoUpdate(LoginRequiredMixin, generic.UpdateView):
    """Actualiza el registro de un equipo"""
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'mantenimiento/nuevo_mantenimiento.html'
    success_url = reverse_lazy('mantenimiento:index')

class MantenimientoCreate(LoginRequiredMixin, generic.CreateView):
    """Vista para agregar un registro de mantenimiento"""
    model = Mantenimiento
    form_class = MantenimientoForm
    context_object_name = 'mantenimiento_objeto'
    template_name = 'mantenimiento/nuevo_mantenimiento.html'
    success_url = reverse_lazy('mantenimiento:index')

class BusquedaMantenimiento(LoginRequiredMixin, generic.ListView):
    """Busca un Mantenimiento"""
    model = Mantenimiento
    context_object_name = 'mantenimiento_objeto'
    template_name = 'mantenimiento/busqueda_mantenimiento.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Mantenimiento.objects.filter(
            Q(id_mantenimiento__icontains=query) | Q(fecha__icontains=query) | Q(descripcion__icontains=query) |
            Q(id_empleado__id_empleado__icontains=query) | Q(id_equipo__id_equipo__icontains=query) | 
            Q(id_tipo_mantenimiento__nombre_tipo_mantenimiento__icontains=query) | Q(id_tipo_mantenimiento__id_tipo_mantenimiento__icontains=query) |
            Q(id_empleado__nombre__icontains=query)
        ) 
        return object_list

def PDF(request, id_mantenimiento):
    """Muestra al Mantenimiento seleccionado en un PDF y las opciones de Guardar dicho PDF y/o Imprimirlo"""
    descripcion_mantenimiento = Mantenimiento.objects.get(pk=id_mantenimiento)
    hora = datetime.now()
    """format = hora.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M')"""
    data = {
            'descripcion_mantenimiento': descripcion_mantenimiento,
            'fechaHora' : hora,
            
        }
    pdf = render_to_pdf('mantenimiento/pdf_mantenimiento.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def generador(request):
    """
    Termina de generar codigo
    """
    if request.method == 'POST':
        print('llego')
        if 'letras' in request.POST:
            letras = request.POST['letras'].upper()
            anio = str(date.today().year)[:2]
            numero = str(Mantenimiento.objects.filter(id_mantenimiento__startswith=letras+anio)
                         .count()+1).zfill(3)
            codigo = letras+anio+numero
            return HttpResponse(codigo)
    return HttpResponse('FAIL!!!!!')

class BodegatoUpdate(LoginRequiredMixin, generic.UpdateView):
    """Actualiza el registro de un equipo"""
    model = Bodega
    form_class = BodegaForm
    template_name = 'mantenimiento/nuevo_bodega.html'
    success_url = reverse_lazy('mantenimiento:index')

class BodegatoCreate(LoginRequiredMixin, generic.CreateView):
    """Vista para agregar un registro de mantenimiento"""
    model = Bodega
    form_class = BodegaForm
    context_object_name = 'mantenimiento_objeto'
    template_name = 'mantenimiento/nuevo_bodega.html'
    success_url = reverse_lazy('mantenimiento:index')

def generador_bodega(request):
    """
    Termina de generar codigo
    """
    if request.method == 'POST':
        print('llego a obtener bodega')
        if 'letras' in request.POST:
            letras = request.POST['letras'].upper()
            anio = str(date.today().year)[:2]
            numero = str(Bodega.objects.filter(id_bodega__startswith=letras+anio)
                         .count()+1).zfill(3)
            codigo = letras+anio+numero
            return HttpResponse(codigo)
    return HttpResponse('FAIL!!!!!')
