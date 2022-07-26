from django import forms
from django.forms import fields

from .models import Listado

class ListadoForm(forms.ModelForm):
    class Meta:
        model = Listado
        fields = '__all__'