from django.shortcuts import render

from users.models import Profile
from .models import StockValue

import datetime

# Create your views here.

def home(request):
    times = []
    values = []
    current_value = get_current_stock_value()

    users = Profile.objects.order_by('-pushups')
    print(users)

    queryset = StockValue.objects.order_by('time')
    for stock in queryset:
        times.append(stock.time.strftime("%m-%d %I:%M%p"))
        values.append(float(stock.value))

    print(values)
    context = {
        'times': times,
        'values': values,
        'users': users,
        'current_value': current_value
    }

    return render(request, 'pushup/index.html', context=context)

def get_current_stock_value():
    return float(StockValue.objects.order_by('-time').first().value)