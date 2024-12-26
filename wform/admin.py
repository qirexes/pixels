from django.contrib import admin
from .models import BankFormSubmission

admin.site.register(BankFormSubmission)


from django.contrib import admin
from .models import SingleInput

@admin.register(SingleInput)
class SingleInputAdmin(admin.ModelAdmin):
    list_display = ['input_value', 'id']  # Customize what columns are shown in the admin list
    search_fields = ['input_value']  # Add search functionality
