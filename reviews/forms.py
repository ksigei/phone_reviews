from django import forms
from django.forms import TextInput, Textarea, FileInput
from .models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'image']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'category': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'form-control'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'text': Textarea(attrs={'class': 'form-control'}),
            'rating': TextInput(attrs={'class': 'form-control'}),
        }
