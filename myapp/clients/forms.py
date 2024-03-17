from django import forms

from .models import Service, Client


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
