from django import forms
from.models import Cart

class Quantity(forms.Form):
    quantity=forms.IntegerField()