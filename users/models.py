from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.TextField(max_length=20)
    pushups = models.DecimalField(max_digits=5, decimal_places=3)
    isEnabled = models.BooleanField(default=False)
    party = models.TextField(max_length=20)

    def __str__ (self):
        return f"{self.user.username}'s Profile"