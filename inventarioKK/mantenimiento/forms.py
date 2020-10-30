"""Formularios de la app """
from django import forms
from .models import Mantenimiento, Bodega, MantenimientoPorBodega

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

class BodegaForm(forms.ModelForm):
    """
    Formulario Recurso de bodega
    """
    class Meta:
        """
        Especificaciones
        """
        model = Bodega

        fields = [
            'id_bodega',
            'nombre_recurso',
            'descripcion',
            'id_tipo_recurso',
        ]
        labels = {
            'id_bodega':'Codigo',
            'nombre_recurso':'Recurso',
            'descripcion':'Descripcion',
            'id_tipo_equipo':'Tipo de Recurso',
        }
        widgets = {
            'id_bodega':forms.TextInput(attrs={'class':'form-control',
                                               'type':'text',
                                               'placeholder':'codigo',
                                               'name':'id_bodega',
                                               'id':'id_bodega',
                                               'readonly':'readonly'}),
            'nombre_recurso':forms.TextInput(attrs={'class':'form-control',
                                               'type':'text',
                                               'placeholder':'Nombre del Recurso',
                                               'name':'nombre_recurso',
                                               'id':'nombre_recurso',
                                               'onkeyup':'PasarValorBodega("nombre_recurso", "id_tipo_recurso", "id_bodega","/mantenimiento/generador_bodega/")'}),
            'descripcion':forms.Textarea(attrs={'rows':'3'}),
            'id_tipo_recurso':forms.Select(attrs={'class':'custom-select',
                                                  'name':'id_tipo_recurso',
                                                  'id':'id_tipo_recurso',
                                                  'onchange':'PasarValorBodega("nombre_recurso", "id_tipo_recurso", "id_bodega","/mantenimiento/generador_bodega/")'}),
        }

class MantenimientoPorBodegaForm(forms.ModelForm):
     class Meta:
        """
        Especificaciones
        """
        model = MantenimientoPorBodega

        fields = [
            'id_mantenimiento_por_bodega',
            'id_mantenimiento',
            'id_bodega',
        ]
        labels = {
            'id_mantenimiento_por_bodega':'Codigo',
            'id_mantenimiento':'Codigo de mantenimiento',
            'id_bodega':'Codigo de bodega',
        }
        widgets = {
            'id_mantenimiento':forms.Select(attrs={'class':'custom-select',
                                                        'name':'id_mantenimiento',
                                                        'id':'id_mantenimiento',
                                                        }),
                'id_bodega':forms.Select(attrs={'class':'choice-in-line',
                                                  'name':'id_bodega',
                                                  'id':'id_bodega',
                                                  }),
        }
