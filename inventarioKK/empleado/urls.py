from django.urls import path
from . import views

app_name = 'empleado'
urlpatterns = [
    path('', views.Indice.as_view(), name='mensaje_empleado'),
    path('<int:pk>/', views.DescripcionEmpleado.as_view(), name='des_em'),
    path('nuevo_empleado/', views.CrearEmpleado.as_view(), name='nuevo_empleado'),
    ]