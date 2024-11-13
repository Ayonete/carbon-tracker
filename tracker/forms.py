from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import CarbonFootprintRecord
from django.core import validators

class addFootprintForm(forms.ModelForm):
    class Meta:
        model = CarbonFootprintRecord
        fields = '__all__'
        exclude = ['user', 'total_footprint', 'date_recorded']
        widgets = {
            'date_recorded': forms.HiddenInput(),
        }