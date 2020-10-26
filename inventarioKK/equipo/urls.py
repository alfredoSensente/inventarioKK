from django.urls import path
from . import views
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

app_name = 'equipo'
urlpatterns = [
    path('', views.ListaDeEquipos.as_view(), name='lista_de_equipos'),
    path('inicio/', views.Inicio.as_view(), name='inicio'),
    path('nuevo_equipo/', views.EquipoCreate.as_view(), name='nuevo_equipo'),
    path('busqueda_equipo/', views.BusquedaEquipo.as_view(), name='busqueda_equipo'),
    path('generador/', views.generador, name='generador'),
    path('<str:pk>/', views.DescripcionEquipo.as_view(), name='des_equipo'),
    path('editar_equipo/<str:pk>/', views.EquipoUpdate.as_view(), name='editar_equipo'),
    path('<str:id_equipo>/PDF/', views.PDF, name='PDF'),
    path('<str:id_equipo>/QR/', views.QR, name='QR'),
    
]
