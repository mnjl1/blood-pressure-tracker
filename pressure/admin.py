from pyexpat import model
from django.contrib import admin
from .models import BloodPressure

class BloodPressureAdmin(admin.ModelAdmin):
    list_display = ('user', 'systolic_pressure', 'diastolic_pressure', 'heart_rate')
    list_filter = ('user', )

admin.site.register(BloodPressure, BloodPressureAdmin)
