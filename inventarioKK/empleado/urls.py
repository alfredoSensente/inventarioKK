from django.urls import path
from . import views

app_name = 'empleado'
urlpatterns = [
    path('', views.mensaje_empleado, name='mensaje_empleado'), 
    path('<int:id_empleado>/', views.descripcion_empleado, name = 'des_em'),
    ]