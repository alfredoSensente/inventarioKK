'''Formularios de Empleado'''
from django import forms
from .models import Empleado
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from datetime import date

class EmpleadoForm(forms.ModelForm):
    """Formulario para agregar un nuevo empleado"""
    class Meta:
        """Especificaciones"""
        model = Empleado

        fields = [
            'id_empleado',
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'dui',
            'nit',
            'telefono_fijo',
            'id_cargo',
            'id_sexo',
            'id_estado_empleado',
            'id_ubicacion',
        ]

        labels = {
            'id_empleado':'Codigo',
            'nombre':'Nombres',
            'apellido':'Apellidos',
            'fecha_nacimiento':'Fecha de Nacimiento',
            'dui':'DUI',
            'nit':'NIT',
            'telefono_fijo':'Teléfono Fijo:',
            'id_cargo':'ID CARGO',
            'id_sexo':'Sexo',
            'id_estado_empleado':'Estado del Empleado',
            'id_ubicacion':'Ubicación',
        }
        widgets = {
            'id_empleado':forms.TextInput(attrs={'class':'form-control',
                                            'type':'text',
                                            'placeholder':'codigo',
                                            'name':'codigo',
                                            'id':'codigo'}),
            'nombre':forms.TextInput(attrs={'class':'form-control',
                                            'type':'text',
                                            'placeholder':'Nombres',
                                            'name':'nombre',
                                            'id':'nombre',
                                            'onkeyup':'PasarValor("nombre","apellido","codigo",path)'}),
            'apellido':forms.TextInput(attrs={'class':'form-control',
                                              'type':'text',
                                              'placeholder':'Apellidos',
                                              'name':'apellido',
                                              'id':'apellido',
                                              'onkeyup':'PasarValor("nombre","apellido","codigo",path)'}),
            'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control',
                                                      'type':'date',
                                                      'placeholder':'Fecha',
                                                      'name':'fecha_nacimiento'}),
            'dui':forms.TextInput(attrs={'type':'number',
                                                    'class':'form-control',
                                                    'name':'dui',
                                                    'placeholder':'########'}),
            'nit':forms.TextInput(attrs={'type':'number',
                                                    'class':'form-control',
                                                    'name':'nit',
                                                    'placeholder':'########'}),
            'telefono_fijo':forms.TextInput(attrs={'type':'number',
                                                    'class':'form-control',
                                                    'name':'telefono_fijo',
                                                    'placeholder':'########'}),
            'id_cargo':forms.Select(attrs={'class':'custom-select',
                                          'name':'cargo'}),
            'id_sexo':forms.Select(attrs={'class':'custom-select',
                                          'name':'sexo'}),
            'id_estado_empleado':forms.Select(attrs={'class':'custom-select',
                                          'name':'estado_empleado'}),
            'id_ubicacion':forms.Select(attrs={'class':'custom-select',
                                          'name':'ubicacion'}),
        }

    def clean_fecha_nacimiento(self):
        cleaned_data = super().clean()
        dob = cleaned_data.get("fecha_nacimiento")
        today = date.today()
        if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('Must be at least 18 years old to register')
        return dob
       