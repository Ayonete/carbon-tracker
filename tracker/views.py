from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from .forms import  addFootprintForm
from .models import *
from .models import CarbonFootprintRecord
import json
from django.shortcuts import get_object_or_404, redirect
# Create your views here.


def home(request):
    records = CarbonFootprintRecord.objects.all().order_by('-date_recorded')

    dates = [record.date_recorded.strftime('%Y-%m-%d') for record in records]
    footprints = [record.total_footprint for record in records]

    context = {
        'records': records,
        'footprints': json.dumps(footprints),
        'dates': json.dumps(dates),
    }
    return render(request, 'tracker/home.html', context)

def add_record(request):
    if request.method == 'POST':
        form = addFootprintForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Footprint record added successfully')
            return redirect('home')
    else:
        form = addFootprintForm()
    return render(request, 'tracker/add_record.html', {'form': form})


# views.py


def edit_record(request, record_id):
    record = get_object_or_404(CarbonFootprintRecord, pk=record_id)
    
    if request.method == 'POST':
        form = addFootprintForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = addFootprintForm(instance=record)
    
    return render(request, 'tracker/edit_record.html', {'form': form})


# views.py
from django.views.decorators.http import require_POST

@require_POST
def delete_record(request, record_id):
    record = get_object_or_404(CarbonFootprintRecord, pk=record_id)
    record.delete()
    return redirect('home')



