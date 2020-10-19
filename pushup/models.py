from django.db import models
from django.utils import timezone

# Create your models here.

def get_time():
    return timezone.localtime(timezone.now())

class StockValue(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=3)
    time = models.DateTimeField(default=get_time)

    def __str__(self):
        return f"Price at {self.time}"