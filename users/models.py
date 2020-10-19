from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    key = models.TextField(max_length=20)
    pushups = models.DecimalField(max_digits=5, decimal_places=3)
    isEnabled = models.BooleanField(default=False)
    party = models.TextField(max_length=20)
    first_name = models.TextField(blank=True, null=True, max_length=25)
    last_name = models.TextField(blank=True, null=True, max_length=25)

    def __str__ (self):
        return f"A Profile"