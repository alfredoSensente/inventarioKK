"""urls de mantenimiento"""
from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('generador/', views.generador, name='generador'),
    path('nuevo_mantenimiento/', views.MantenimientoCreate.as_view(), name='nuevo'),
    path('editar_mantenimiento/<str:pk>/', views.MantenimientoUpdate.as_view(), name='editar'),
    path('descripcion_mantenimiento/<str:pk>', views.DescripcionMatenimiento.as_view(), name='descripcion'),
    path('<str:pk>/', views.DescripcionMatenimiento.as_view(), name='descripcion'),
    path('<str:id_equipo>/PDF/', views.PDF, name='PDF'),

]
