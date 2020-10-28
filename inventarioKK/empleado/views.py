"""Vistas de la Aplicacion Empleado"""
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Empleado
from .forms import EmpleadoForm
from django.shortcuts import render
from .utils import render_to_pdf
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Indice(LoginRequiredMixin, generic.ListView):
    """Vista Genèrica de Tabla de Empleados"""
    template_name = 'empleado/e_index.html'
    context_object_name = 'lista_empleado'
    model = Empleado
    paginate_by = 5

class DescripcionEmpleado(LoginRequiredMixin, generic.DetailView):
    """Muestra una descripcion de cada Empleado"""
    template_name = 'empleado/descripcion_e.html'
    context_object_name = 'descripcion_empleado'
    model = Empleado

class CrearEmpleado(LoginRequiredMixin, generic.CreateView):
    """Muestra el formulario para crear un nuevo Empleado"""
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/nuevo_empleado.html'
    success_url = reverse_lazy('empleado:mensaje_empleado')

    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return HttpResponseRedirect(reverse_lazy('empleado:mensaje_empleado'))
        else:
            return render(request, 'empleado/nuevo_empleado.html',
                          {'form': form, 'error_date': 'Estas intentando contratar a un menor, pervertido!'})

class EditarEmpleado(LoginRequiredMixin, generic.UpdateView):
    """Actualiza el registro de un Empleado"""
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/nuevo_empleado.html'
    success_url = reverse_lazy('empleado:mensaje_empleado')

class EliminarEmpleado(LoginRequiredMixin, generic.DeleteView):
    """Elimina un Empleado"""
    model = Empleado
    context_object_name = 'descripcion_empleado'
    template_name = 'empleado/eliminar_empleado.html'
    success_url = reverse_lazy('empleado:mensaje_empleado')

class BusquedaEmpleado(LoginRequiredMixin, generic.ListView):
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

def EmpleadoPDF(request, id_empleado):
    """Muestra al Empleado seleccionado en un PDF y las opciones de Guardar dicho PDF y/o Imprimirlo"""
    descripcion_empleado = Empleado.objects.get(pk=id_empleado)
    hora = datetime.now()
    """format = hora.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M')"""
    data = {
            'descripcion_empleado': descripcion_empleado,
            'fechaHora' : hora,
            
        }
    pdf = render_to_pdf('empleado/pdf_empleado.html', data)
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
            numero = str(Empleado.objects.filter(id_empleado__startswith=letras+anio).count()+1).zfill(3)
            codigo = letras+anio+numero
            return HttpResponse(codigo)
    return HttpResponse('FAIL!!!!!')
