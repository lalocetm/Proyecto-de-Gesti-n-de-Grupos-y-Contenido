from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']
        widgets = {
            'date': forms.HiddenInput(),  # Hacer invisible el campo date
        }