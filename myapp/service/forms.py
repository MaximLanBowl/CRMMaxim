from django import forms
from django.forms import ModelForm
from .models import Service


class ServiceForm(forms.ModelForm):
    model = Service
    fields = ['name', 'description']


