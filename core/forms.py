from django import forms
from .models import User, Produto
from .choices import categorias


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_photo']

        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'first_name', 'type': 'text', 'class': 'validate', 'data-length': 30}),
            'last_name': forms.TextInput(attrs={'id': 'last_name', 'type': 'text', 'class': 'validate', 'data-length': 30}),
            'user_photo': forms.FileInput(attrs={'accept': 'image/x-png, image/jpeg'})
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['title', 'photo_medium', 'photo_thumb', 'amount', 'price', 'description', 'ingredients', 'category',
                  'preparation_time', 'sizes']

        widgets = {
            'title': forms.TextInput(attrs={'id': 'icon_prefix', 'type': 'text', 'class': 'validate', 'data-length': 30}),
            'photo_medium': forms.FileInput(attrs={'accept': 'image/x-png, image/jpeg'}),
            'amount': forms.NumberInput(attrs={'id': 'amount', 'type': 'number', 'class': 'validate'}),
            'price': forms.NumberInput(attrs={'id': 'price', 'type': 'number', 'class': 'validate'}),
            'description': forms.Textarea(attrs={'id': 'description', 'class': 'materialize-textarea', 'data-length': 300}),
            'ingredients': forms.SelectMultiple(attrs={'id': 'description', 'value': '-1'}),
            'category': forms.Select(choices=categorias),
            'sizes': forms.SelectMultiple(),
            'preparation_time': forms.NumberInput(attrs={'id': 'preparation_time'})
        }