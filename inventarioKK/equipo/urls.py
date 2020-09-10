from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_de_equipos, name='lista_de_equipos')
]