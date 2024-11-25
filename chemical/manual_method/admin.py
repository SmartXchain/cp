# manual_method/admin.py

from django.contrib import admin
from .models import ManualMethod


@admin.register(ManualMethod)
class ManualMethodAdmin(admin.ModelAdmin):
    list_display = ('method_number', 'process_type', 'temperature_min', 'temperature_max', 'time_immersion_min', 'time_immersion_max', 'test_required')
    list_filter = ('process_type',)
    search_fields = ('method_number', 'process_type')
