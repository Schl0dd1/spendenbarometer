from django import forms
from django.forms import ModelForm
from .models import Konto, Buchung

#Create a form

class NeuerEintrag(ModelForm):
    class Meta: 
        model = Buchung
        fields = ('__all__')

class NeuesKonto(forms.Form):
    class Meta:
        model = Konto
        fields = ('konto_name')
        
    #name = forms.CharField(max_length=100)