from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    """Formulario para agregar un nuevo equipo"""
    class Meta:
        """Especificaciones"""
        model = Equipo

        fields = [
            'id_tipo_equipo',
            'id_marca',
            'id_estado_equipo',
            'id_ubicacion',
            'descripcion',
         ]

        labels = {
            'id_tipo_equipo':'Tipo del equipo',
            'id_marca':'Marca',
            'id_estado_equipo':'Estado del equipo',
            'id_ubicacion':'Ubicacion',
            'descripcion':'Descripcion',
        }

        widgets = {
            'id_tipo_equipo':forms.Select(attrs={'class':'custom-select',
                                          'name':'tipo del equipo'}),
            'id_marca':forms.Select(attrs={'class':'custom-select',
                                               'name':'marca'}),
            'id_estado_equipo':forms.Select(attrs={'class':'custom-select',
                                                  'name':'estado del equipo'}),
            'id_ubicacion':forms.Select(attrs={'class':'custom-select',
                                               'name':'ubicacion'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control',
                                              'type':'text',
                                              'placeholder':'Descripcion del equipo',
                                              'name':'descripcion'}),
        }