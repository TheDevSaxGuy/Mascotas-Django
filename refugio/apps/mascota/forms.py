from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model=Mascota

        fields=[
            'nombre',
            'edad_aproximada',
            'sexo',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        lables={
            'nombre':' Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona':'Adoptante',
            'vacuna': 'Vacunas',
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.NumberInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate':forms.DateInput(attrs={'class':'form-control'}),
            'persona':forms.Select(attrs={'class':'form-control'}),
            'vacuna':forms.CheckboxSelectMultiple(),
        }