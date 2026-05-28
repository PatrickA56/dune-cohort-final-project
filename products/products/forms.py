from django import forms 
from .models import Product, Category 


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product name'}),
            'price': forms.NumberInput(attrs={'min': '0'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category 
        fields = '__all__'