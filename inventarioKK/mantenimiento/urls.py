"""urls de mantenimiento"""
from django.urls import path
from . import views

app_name = 'mantenimiento'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>/', views.DescripcionMatenimiento.as_view(), name='descripcion'),
    path('nuevo_correctivo/', views.CorretivoCreate.as_view(), name='nuevo_correctivo'),
    path('borrar_mantenimiento/<int:pk>/', views.MantenimientoDelete.as_view(), name='borrar_mantenimiento'),
]
