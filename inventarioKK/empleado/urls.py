from django.urls import path
from . import views

app_name = 'empleado'
urlpatterns = [
    path('', views.Indice.as_view(), name='mensaje_empleado'),
    path('busqueda_empleado/', views.BusquedaEmpleado.as_view(), name='busqueda_empleado'),
    path('nuevo_empleado/', views.CrearEmpleado.as_view(), name='nuevo_empleado'),
    path('generador/', views.generador, name='generador'),
    path('<str:pk>/', views.DescripcionEmpleado.as_view(), name='des_em'),
    path('editar_empleado/<str:pk>/', views.EditarEmpleado.as_view(), name='editar_empleado'),
    path('eliminar_empleado/<str:pk>/', views.EliminarEmpleado.as_view(), name='eliminar_empleado'),
]
