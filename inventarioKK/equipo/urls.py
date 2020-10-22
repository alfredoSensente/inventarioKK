from django.urls import path
from . import views
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

app_name = 'equipo'
urlpatterns = [
    path('', views.ListaDeEquipos.as_view(), name='lista_de_equipos'),
    path('nuevo_equipo/', views.EquipoCreate.as_view(), name='nuevo_equipo'),
    path('<int:pk>/', views.DescripcionEquipo.as_view(), name='des_equipo'),
    path('editar_equipo/<int:pk>/', views.EquipoUpdate.as_view(), name='editar_equipo'),
    path('busqueda_equipo/', views.BusquedaEquipo.as_view(), name='busqueda_equipo'),
    path('<int:id_equipo>/PDF/', views.PDF, name='PDF'),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

]