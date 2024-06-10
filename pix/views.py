from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm, ProfilePictureForm, ProfileSettingsForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .models import Balance, Notification, CollectionClickLog, Deposit
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from .models import Image, Category, Profile, ImageFile, Withdrawal
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import User  # Assuming 'User' is in your app's models.py




def index(request):
    template = loader.get_template('pix/index.html')
    context = {}
    rendered_template = template.render(context, request)
    return HttpResponse(rendered_template)

# def collection_purchase(request):
#     template = loader.get_template('pix/collection_purchase.html')
#     context = {}
#     rendered_template = template.render(context, request)
#     return HttpResponse(rendered_template)


@login_required
def collection_purchase(request):
    if request.method == "POST":
        # Log the click
        CollectionClickLog.objects.create(user=request.user)
        # Handle the purchase logic here
        # ...
        return redirect('pix:collection_purchase')
    return render(request, 'pix/collection_purchase.html')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('pix:dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'pix/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    form.add_error(None, "Invalid username or password")
                else:
                    auth_login(request, user)
                    return redirect('pix:dashboard')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'pix/login.html', {'form': form})

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('pix:index')
    else:
        return redirect('pix:login')






@login_required
def collections(request):
    user_images = Image.objects.filter(user=request.user)
    categories = set(image.category for image in user_images)
    collections_preview = {category: user_images.filter(category=category).first() for category in categories}
    
    return render(request, 'pix/collections.html', {'collections_preview': collections_preview})


@login_required
def full_collection(request, category_id):
    user_images = Image.objects.filter(user=request.user, category_id=category_id)
    images_data = [{'name': image.name, 'price': image.price} for image in user_images]
    
    return JsonResponse({'images': images_data})


@login_required
# def create(request):
#     upload_cost = 180
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             user_balance = Balance.objects.get_or_create(user=request.user)[0]

#             if user_balance.balance >= upload_cost:
#                 user_balance.balance -= upload_cost
#                 user_balance.save()

#                 image = form.save(commit=False)
#                 image.user = request.user
#                 image.save()

#                 # here
#                 images = request.FILES.getlist('images')
#                 for img in images:
#                     ImageFile.objects.create(image=img, image_info=image)

#                 messages.success(request, 'Image uploaded successfully and amount deducted from your balance.')
#                 return redirect('pix:explore')
#             else:
#                 messages.error(request, 'Insufficient balance to upload the image.')
#         else:
#             messages.error(request, 'Invalid form submission.')
#     else:
#         form = ImageUploadForm()
#     return render(request, 'pix/create.html', {'form': form})

def create(request):
    upload_cost = 180
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_balance = Balance.objects.get_or_create(user=request.user)[0]

            if user_balance.balance >= upload_cost:
                user_balance.balance -= upload_cost
                user_balance.save()

                # Save the main Image object
                image = form.save(commit=False)
                image.user = request.user
                image.save()

                # Handle multiple file uploads for ImageFile
                images = request.FILES.getlist('images')
                for img in images:
                    ImageFile.objects.create(image=img, image_info=image)

                messages.success(request, 'Image uploaded successfully and amount deducted from your balance.')
                return redirect('pix:explore')
            else:
                messages.error(request, 'Insufficient balance to upload the image.')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = ImageUploadForm()
    return render(request, 'pix/create.html', {'form': form})

# def explore(request):
#     categories = Category.objects.all()
#     images_by_category = {}
#     for category in categories:
#         images = ImageFile.objects.filter(image_info__category=category)
#         images_by_category[category.name] = images

#     return render(request, 'pix/explore.html', {'images_by_category': images_by_category})


#Elvis Code >>>>>>>>>>>>>>>>>>>>>>
def explore(request):
    categories = Category.objects.all()
    images_by_category = {}

    for category in categories:
        image = ImageFile.objects.filter(image_info__category=category).first()
        if image:
            images_by_category[category.name] = image

    return render(request, 'pix/explore.html', {'images_by_category': images_by_category})

#Elvis End >>>>>>>>>>>>>>>>>>>>>>>>


def view_collections(request, image_name):
    images_info = Image.objects.filter(name=image_name)
    images = ImageFile.objects.filter(image_info__in=images_info)
    return render(request, 'pix/view_collections.html', {'image_name': image_name, 'images': images})

@login_required
def dashboard(request):
    user_balance = Balance.objects.get_or_create(user=request.user)[0]
    user_image_count = Image.objects.filter(user=request.user).count()

    context = {
        'user_balance': user_balance,
        'user_image_count': user_image_count,
    }
    
    return render(request, 'pix/dashboard.html', context)

@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user)
    context = {'notifications': user_notifications}
    return render(request, 'pix/notifications.html', context)

def privacy(request):
    template = loader.get_template('pix/privacy.html')
    context = {}
    rendered_template = template.render(context, request)
    return HttpResponse(rendered_template)

def Terms(request):
    template = loader.get_template('pix/Terms.html')
    context = {}
    rendered_template = template.render(context, request)
    return HttpResponse(rendered_template)

# def settings_view(request):
#     profile = get_object_or_404(Profile, user=request.user)
#     if request.method == 'POST':
#         profile_form = ProfileSettingsForm(request.POST, instance=profile)
#         picture_form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('pix:dashboard')
#     else:
#         form = ProfilePictureForm()
#     return render(request, 'pix/settings.html', {'form': form})


def settings_view(request):
    # Retrieve the profile if it exists, otherwise create a new one
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile_form = ProfileSettingsForm(request.POST, instance=request.user)
        picture_form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid() and picture_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            picture_form.save()
            return redirect('pix:dashboard')
    else:
        profile_form = ProfileSettingsForm(instance=request.user)
        picture_form = ProfilePictureForm(instance=profile)
    
    return render(request, 'pix/settings.html', {'profile_form': profile_form, 'picture_form': picture_form})

@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')
    notifications.filter(read=False).update(read=True)
    return render(request, 'notifications.html', {'notifications': notifications})

@login_required
def dashboard_view(request):
    user = request.user
    user_balance = Balance.objects.filter(user=user).first()
    return render(request, 'dashboard.html', {'user': user, 'user_balance': user_balance})


    # if request.method == 'POST':
    #     form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.profile)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('settings')  # Adjust the redirect as needed
    # else:
    #     form = ProfilePictureForm(instance=request.user.profile)

    # return render(request, 'settings.html', {'form': form})
    if request.method == 'POST':
        profile_form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')  # Redirect to user dashboard
    else:
        profile_form = ProfilePictureForm(instance=request.user.profile)
    return render(request, 'settings.html', {'profile_form': profile_form})





# def deposit(request):
#     if request.method == 'POST':
#         amount = request.POST.get('amount')
#         user_id = request.POST.get('user_id')

#         # Save the deposit
#         deposit = Deposit.objects.create(amount=amount, user_id=user_id)

#         return redirect('admin:pix_deposit_changelist')  # Redirect to admin page after deposit

#     return JsonResponse({'status': 'error'})


@login_required
def collection_purchase(request):
    if request.method == "POST":
        # Log the click
        CollectionClickLog.objects.create(user=request.user)
        # Handle the purchase logic here
        # ...
        return redirect('pix:collection_purchase')
    return render(request, 'pix/collection_purchase.html')


# Elvis CODE >>>>>>

@login_required
def deposit(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        user = request.user

        # Optional data validation (e.g., check amount is positive)
        if not amount or float(amount) <= 0:
            return render(request, 'dashboard.html', {'error_message': 'Invalid amount'})

        # Try saving the deposit
        try:
            deposit = Deposit.objects.create(amount=amount, user=user)
            return HttpResponseRedirect(request.path_info + '?success=1')
        except Exception as e:
            print(f"Error saving deposit: {e}")
            return render(request, 'dashboard.html', {'error_message': 'An error occurred while saving the deposit'})

    success_message = 'Deposit successful' if request.GET.get('success') == '1' else ''
    return render(request, 'dashboard.html', {'success_message': success_message})
    

    # ... rest of your code
#ELVIS CODE END >>>>



@login_required
def withdraw(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        try:
            amount = float(amount)
        except ValueError:
            messages.error(request, 'Invalid amount.')
            return redirect('pix:dashboard')  # Replace with your desired URL

        user_balance = request.user.balance.balance
        if user_balance >= amount:
            withdrawal_amount = amount + (amount * 0.1)
            request.user.balance.balance -= withdrawal_amount
            request.user.balance.save()

            # Create a new Withdrawal instance
            withdrawal = Withdrawal.objects.create(
                user=request.user,
                amount=amount
            )

            messages.success(request, f"You have successfully withdrawn {amount}.")
            return redirect('pix:dashboard')  # Replace with your desired URL
        else:
            messages.error(request, "You don't have enough balance to withdraw this amount.")
            return redirect('pix:dashboard')  # Replace with your desired URL
    else:
        return redirect('pix:dashboard')  # Replace with your desired URL