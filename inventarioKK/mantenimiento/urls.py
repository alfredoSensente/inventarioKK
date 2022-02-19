"""urls de mantenimiento"""
from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('generador/', views.generador, name='generador'),
    path('generador_bodega/', views.generador_bodega, name='generador_bodega'),
    path('busqueda_mantenimiento/', views.BusquedaMantenimiento.as_view(), name='busqueda_mantenimiento'),
    path('nuevo_mantenimiento/', views.MantenimientoCreate.as_view(), name='nuevo'),
    path('index_bodega/', views.BodegaIndex.as_view(), name='index_bodega'),
    path('nuevo_bodega/', views.BodegatoCreate.as_view(), name='nuevo_bodega'),
    path('busqueda_bodega/', views.BodegaBusqueda.as_view(), name='busqueda_bodega'),
    path('nuevo_mantenimientoporbodega/', views.MantenimientoPorBodegaCreate.as_view(), name='nuevo_mantenimientoporbodega'),
    path('editar_mantenimiento/<str:pk>/', views.MantenimientoUpdate.as_view(), name='editar'),
    path('descripcion_mantenimiento/<str:pk>/', views.DescripcionMatenimiento.as_view(), name='descripcion'),
    path('<str:pk>/', views.DescripcionMatenimiento.as_view(), name='descripcion'),
    path('editar_bodega/<str:pk>/', views.BodegatoUpdate.as_view(), name='editar_bodega'),
    path('descripcion_bodega/<str:pk>/', views.BodegaDescripcion.as_view(), name='descripcion_bodega'),
    


]
