from django import forms

from .models import *

class RezervaceForm(forms.ModelForm):
    class Meta:
        model = Rezervace
        fields = ['pokoj', 'pocet_noci', 'jmeno', 'adresa', 'datum_prijezdu', 'datum_odjezdu']

        widgets = {
            'pokoj' : forms.Select(
                attrs={
                    'class': 'form-control inputstl'
                }
            ),
            'pocet_noci': forms.NumberInput(
                attrs={
                    'class': 'form-control inputstl'
                }
            ),
            'jmeno': forms.TextInput(
                attrs={
                    'class': 'form-control inputstl'
                }
            ),
            'adresa': forms.TextInput(
                attrs={
                    'class': 'form-control inputstl'
                }
            ),
            'datum_prijezdu' : forms.SelectDateWidget(
                attrs={
                    'class': 'form-control inputstl'
                }
            ),
            'datum_odjezdu': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control inputstl'
                }
            ),
        }

