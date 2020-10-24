from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    """Formulario para agregar un nuevo equipo"""
    class Meta:
        """Especificaciones"""
        model = Equipo

        fields = [
            'id_equipo',
            'id_tipo_equipo',
            'modelo',
            'id_marca',
            'id_estado_equipo',
            'id_ubicacion',
            'descripcion',
            'anho_fabricacion',
         ]

        labels = {
            'id_tipo_equipo':'Tipo del equipo',
            'id_marca':'Marca',
            'id_estado_equipo':'Estado del equipo',
            'id_ubicacion':'Ubicacion',
            'descripcion':'Descripcion',
        }

        widgets = {
            'id_equipo':forms.TextInput(attrs={'class':'form-control',
                                               'type':'text',
                                               'placeholder':'codigo',
                                               'name':'id_equipo',
                                               'id':'id_equipo'}),
            'modelo':forms.TextInput(attrs={'class':'form-control',
                                               'type':'text',
                                               'placeholder':'modelo'}),
            'id_tipo_equipo':forms.Select(attrs={'class':'custom-select',
                                          'name':'tipo del equipo',
                                          'id':'tipo_equipo',
                                          'onchange':'SelectPasarValorEquipo("tipo_equipo","marca","ubicacion","id_equipo",path)'}),
            'id_marca':forms.Select(attrs={'class':'custom-select',
                                               'name':'marca',
                                               'id':'marca',
                                               'onchange':'SelectPasarValorEquipo("tipo_equipo","marca","ubicacion","id_equipo",path)'}),
            'id_estado_equipo':forms.Select(attrs={'class':'custom-select',
                                                  'name':'estado del equipo'}),
            'id_ubicacion':forms.Select(attrs={'class':'custom-select',
                                               'name':'ubicacion',
                                               'id':'ubicacion',
                                               'onchange':'SelectPasarValorEquipo("tipo_equipo","marca","ubicacion","id_equipo",path)'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control',
                                              'type':'text',
                                              'placeholder':'Descripcion del equipo',
                                              'name':'descripcion'}),
            'anho_fabricacion':forms.TextInput(attrs={'class':'form-control',
                                               'type':'text',
                                               'placeholder':'Año Fabricacion'}),
        }