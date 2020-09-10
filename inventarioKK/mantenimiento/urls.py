"""urls de mantenimiento"""
from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_mantenimiento>/', views.descripcion, name='descripcion'),
]
