from django.urls import path
from django.urls import path
from . import views

app_name = 'equipo'
urlpatterns = [
    path('', views.ListaDeEquipos.as_view(), name='lista_de_equipos'),
    path('nuevo_equipo/', views.EquipoCreate.as_view(), name='nuevo_equipo'),
    path('<int:pk>/', views.DescripcionEquipo.as_view(), name='des_equipo'),

]