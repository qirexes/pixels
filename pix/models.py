from django.db import models
from django.contrib.auth.models import User

class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)

    def __str__(self):
        return f"{self.balance}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.name}"
    
class ImageFile(models.Model):
    image = models.ImageField(upload_to='images/')
    image_info = models.ForeignKey(Image, on_delete=models.CASCADE)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.message}"
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')

    def __str__(self):
        return self.user.username


class CollectionClickLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} clicked at {self.timestamp}"
    


class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.amount}'
    

class Withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    withdrawal_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"