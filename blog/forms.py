from django import forms
from .models import *
class AdvertisingForm(forms.ModelForm):
    class Meta:
        model=Advertising
        fields='Advertising_img'
