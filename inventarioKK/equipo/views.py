from django.shortcuts import render
from .models import Equipo, Edificio
from django.views import generic, View
from .forms import EquipoForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from .utils import render_to_pdf
from datetime import datetime
from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import qrcode

# Create your views here.
class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class ListaDeEquipos(LoginRequiredMixin, generic.ListView):
    """vista generica tabla equipos"""
    paginate_by = 5
    template_name= 'equipo/index.html'
    context_object_name = 'lista_equipo'
    model = Equipo
   
class EquipoCreate(LoginRequiredMixin, generic.CreateView):
    """Crear un nuevo equipo"""
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/nuevo_equipo.html'
    success_url = reverse_lazy('equipo:lista_de_equipos')

class DescripcionEquipo(LoginRequiredMixin, generic.DetailView):
    """Muestra una descripcion de cada Equipo"""
    template_name = 'equipo/descripcion_equipo.html'
    context_object_name = 'descripcion_equipo'
    model = Equipo


class EquipoUpdate(LoginRequiredMixin, generic.UpdateView):
    """Actualiza el registro de un equipo"""
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/nuevo_equipo.html'
    success_url = reverse_lazy('equipo:lista_de_equipos')

class BusquedaEquipo(LoginRequiredMixin, generic.ListView):
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
    hora = datetime.now()
    """format = hora.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M')"""
    data = {
            'descripcion_equipo': descripcion_equipo,
            'fechaHora' : hora,
            
        }
    pdf = render_to_pdf('equipo/lista.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def loginpage(request):
    userlogin = "admin"
    passw = "admin"
    if request.method == 'POST':
    		username = request.POST.get('username')
    		password = request.POST.get('password')

    		

    		if userlogin == username and passw == password:
    			"""login(request, user)"""
    			return redirect('equipo:lista_de_equipos')
    		else:
    			messages.info(request, 'Usuario o contraseña incorrectos')

    context = {}
    return render(request, 'equipo/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('equipo:login')

def generador(request):
    """
    Termina de generar codigo
    """
    if request.method == 'POST':
        print('llego')
        if 'letras' in request.POST:
            letras = request.POST['letras'].upper()
            numero = str(Equipo.objects.filter(id_equipo__startswith=letras).count()+1).zfill(3)
            anio = str(date.today().year)
            codigo = letras+anio[:2]+numero
            print(codigo)
            return HttpResponse(codigo)
    return HttpResponse('FAIL!!!!!')

def QR(request, id_equipo):
    descripcion_equipo = Equipo.objects.get(pk=id_equipo)
    img=qrcode.make(f'equipo/{id_equipo}')
    data = {
            'descripcion_equipo': descripcion_equipo,
            'img' : img,
            
        }
    
    return HttpResponse(img.show('code.png'))