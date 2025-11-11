from django import forms
from .models import Categories

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'description'] #Поля для добавления заметок, Заголовок и Текст
