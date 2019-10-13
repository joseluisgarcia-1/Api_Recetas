from django import forms
from apps.recetas.models import Recetas

class RecetasForm(forms.ModelForm):

    class Meta:
        model = Recetas

        fields = [
            'receta',
            'tipo',
            'pasos',
            'ingredientes',
            'descripcion',


        ]
        labels = {
            'receta': 'Nombre receta',
            'tipo': 'Tipo de receta',
            'pasos':'Pasos para preparar la receta',
            'ingredientes':'Ingredientes',
            'descripcion':'Descripcion de la receta',


        }
        widgets = {
            'receta': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class:': 'form-control'}),
            'pasos': forms.Textarea(attrs={'class': 'form-control'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
