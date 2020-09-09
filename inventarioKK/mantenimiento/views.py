from django.shortcuts import render

# Create your views here.
def hola_mundo(request):
    """Muestra la template de Hola Mundo"""
    return render(request, 'mantenimiento/index.html')
