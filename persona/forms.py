from django import forms
from .models import TipoDocumento

class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'nombre'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control mb-3', 'required':'true', 'id':'descripcion'}),
        }
