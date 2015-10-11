# app1/forms.py
from django import forms


class LocationForm(forms.Form):
    city = forms.CharField(label='City', max_length=50)
    country = forms.CharField(label='Country', max_length=2)

    