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
    path('nuevo_bodega/', views.BodegatoCreate.as_view(), name='nueva_bodega'),
    path('editar_mantenimiento/<str:pk>/', views.MantenimientoUpdate.as_view(), name='editar'),
    path('descripcion_mantenimiento/<str:pk>', views.DescripcionMatenimiento.as_view(), name='descripcion'),
    path('<str:pk>/', views.DescripcionMatenimiento.as_view(), name='descripcion'),
    path('<str:id_mantenimiento>/pdf_mantenimiento/', views.PDF, name='pdf_mantenimiento'),
    path('editar_bodega/<str:pk>/', views.BodegatoUpdate.as_view(), name='editar_bodega'),


]
