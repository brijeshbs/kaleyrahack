from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}"

class Breakfast(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='breakfasts')
    dateOfEntry = models.DateField(default=datetime.today().date())

    def __str__(self):
        return f"{self.id}: {self.user} {self.dateOfEntry}"

class Snacks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snacks')
    dateOfEntry = models.DateField(default=datetime.today().date())
    
    def __str__(self):
        return f"{self.id}: {self.user} {self.dateOfEntry}"
