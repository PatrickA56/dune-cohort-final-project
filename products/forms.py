from django import forms 
from .models import Product, Category 


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'category', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Product name',
                'class': 'form-input'
            }),
            'price': forms.NumberInput(attrs={
                'min': '0',
                'class': 'form-input'
            }),
            'stock': forms.NumberInput(attrs={
                'min': '0',
                'class': 'form-input'
            }),
            'category': forms.Select(attrs={
                'class': 'form-input'
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category 
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Category name',
                'class': 'form-input'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Category description',
                'class': 'form-input',
                'rows': 4
            }),
        }
