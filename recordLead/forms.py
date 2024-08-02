from django.core import validators
from django import forms
from .models import Lead

class LeadRegistration(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['customer_name', 'property_type', 'property_area','property_price','schedule']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'property_type': forms.TextInput(attrs={'class':'form-control'}),
            'property_area': forms.TextInput(attrs={'class':'form-control'}),
            'property_price': forms.NumberInput(attrs={'class':'form-control'}),
            'schedule': forms.DateTimeInput(attrs={'type': 'datetime-local','class':'form-control'}),
        }