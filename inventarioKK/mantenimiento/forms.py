"""Formularios de la app Mantenimiento"""
from django import forms
from .models import Mantenimiento

class MantenimientoForm(forms.ModelForm):
    """
    Formulario Mantenimiento
    """
    class Meta:
        """
        Especificaciones
        """
        model = Mantenimiento

        fields = [
            'id_mantenimiento',
            'fecha',
            'descripcion',
            'id_empleado',
            'id_equipo',
            'id_tipo_mantenimiento',
        ]
        labels = {
            'id_mantenimiento':'Codigo',
            'fecha':'Fecha',
            'descripcion':'Descripcion',
            'id_empleado':'Empleado',
            'id_equipo':'Equipo',
            'id_tipo_mantenimiento':'Tipo Mantenimiento',
        }
        widgets = {
            'id_mantenimiento':forms.TextInput(attrs={'class':'form-control',
                                               'type':'text',
                                               'placeholder':'codigo',
                                               'name':'id_mantenimiento',
                                               'id':'id_mantenimiento',
                                               'readonly':'readonly'}),
            'fecha':forms.TextInput(attrs={'class':'form-control',
                                           'type':'date',
                                           'placeholder':'Fecha',
                                           'name':'fecha',
                                           'id':'fecha'}),
            'descripcion':forms.Textarea(attrs={'rows':'3'}),
            'id_empleado':forms.Select(attrs={'class':'custom-select',
                                              'name':'id_empleado',
                                              'id':'id_empleado',
                                              'onchange':'SelectPasarValorEquipo("id_empleado","id_equipo","id_tipo_mantenimiento","id_mantenimiento","/mantenimiento/generador/")'}),
            'id_equipo':forms.Select(attrs={'class':'custom-select',
                                            'name':'id_equipo',
                                            'id':'id_equipo',
                                            'onchange':'SelectPasarValorEquipo("id_empleado","id_equipo","id_tipo_mantenimiento","id_mantenimiento","/mantenimiento/generador/")'}),
            'id_tipo_mantenimiento':forms.Select(attrs={'class':'custom-select',
                                                        'name':'tipo_mantenimiento',
                                                        'id':'id_tipo_mantenimiento',
                                                        'onchange':'SelectPasarValorEquipo("id_empleado","id_equipo","id_tipo_mantenimiento","id_mantenimiento","/mantenimiento/generador/")'}),
        }
