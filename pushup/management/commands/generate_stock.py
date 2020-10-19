from django.core.management.base import BaseCommand, CommandError
from pushup.models import StockValue
import random

def get_current_stock_value():
    return float(StockValue.objects.order_by('-time').first().value)

class Command(BaseCommand):
    help = 'Generate a new stock value'

    def handle(self, *args, **options):
        current_val = get_current_stock_value()
        if current_val <= 0.5:
            new_value = StockValue(value=round(current_val + round(random.uniform(0.0, 0.5), 3), 3))
        if current_val >= 2:
            new_value = StockValue(value=round(current_val + round(random.uniform(-0.15, 0.10), 3), 3))
        else:
            new_value = StockValue(value=round(current_val + round(random.uniform(-0.09, 0.10), 3), 3))
        
        
        new_value.save()