from django import forms

class CreateBankForm(forms.Form):
    name = forms.CharField(max_length=32, widget = (forms.TextInput(attrs={
        'type': 'text', 
        'class': 'form-control', 
        'placeholder': 
        'Generic Bank Name'}
    )))
    address = forms.CharField(max_length=255, widget = (forms.TextInput(attrs={
        'type': 'text', 
        'class': 'form-control', 
        'placeholder': 
        'Generic Bank Address'}
    )))