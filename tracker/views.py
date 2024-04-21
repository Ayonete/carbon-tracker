from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from .forms import  addFootprintForm
from .models import *
from .models import CarbonFootprintRecord
import json
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

@login_required
def home(request):

    latitude = 'default_latitude'
    longitude = 'default_longitude'

    records = CarbonFootprintRecord.objects.filter(user=request.user).order_by('-date_recorded')
    dates = [record.date_recorded.strftime('%Y-%m-%d') for record in records]
    footprints = [record.total_footprint for record in records]
    
    dates_json = json.dumps(dates)
    footprints_json = json.dumps(footprints)
    
    context = {'records': records, 
               'footprints': footprints_json, 
               'dates': dates_json, 

               }
    return render(request, 'tracker/home.html', context)

@login_required
def add_record(request):
    if request.method == 'POST':
        form = addFootprintForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            messages.success(request, 'Footprint record added successfully')
            return redirect('home')
    else:
        form = addFootprintForm()
    return render(request, 'tracker/add_record.html', {'form': form})

# views.py


def edit_record(request, record_id):
    record = get_object_or_404(CarbonFootprintRecord, pk=record_id, user=request.user)
    
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
    record = get_object_or_404(CarbonFootprintRecord, pk=record_id, user=request.user)
    record.delete()
    return redirect('home')



