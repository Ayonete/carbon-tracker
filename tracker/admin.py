from django.contrib import admin

# Register your models here.
from .models import CarbonFootprintRecord

class CarbonFootprintRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_recorded', 'total_footprint')
admin.site.register(CarbonFootprintRecord)
# admin.site.register(Profile)