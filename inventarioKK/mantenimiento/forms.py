"""Formularios de la app Mantenimiento"""
from django import forms
from .models import Correctivo

class CorrectivoForm(forms.ModelForm):
    """Formulario que agregar un nuevo mantenimiento Correctivo"""
    class Meta:
        model = Correctivo

        fields = [
            'id_mantenimiento',
            'id_tipo_correctivo',
            'fecha_correctivo',
            'descripcion',
        ]
        labels = {
            'id_mantenimiento':'Codigo de equipo',
            'id_tipo_correctivo':'Tipo de Correctivo',
            'fecha_correctivo':'Fecha',
            'descripcion':'Descripcion del mantenimiento',
        }
        widgets = {
            'id_mantenimiento':forms.Select(attrs={'class':'custom-select',
                                                   'name':'mantenimiento'}),
            'id_tipo_correctivo':forms.Select(attrs={'class':'custom-select',
                                                     'name':'tipo_correctivo'}),
            'fecha_correctivo':forms.TextInput(attrs={'class':'form-control',
                                                      'type':'date',
                                                      'placeholder':'Fecha',
                                                      'name':'fecha_nacimiento'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control',
                                                'type':'text',
                                                'name':'descripcion'}),
        }
