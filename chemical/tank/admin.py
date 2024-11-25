# tank/admin.py

from django.contrib import admin
from .models import Tank


@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    list_display = (
        'tank_number', 'process_description', 'temperature_min', 'temperature_max',
        'uses_rectifier', 'time_immersion_min', 'time_immersion_max', 'test_required'
    )
    list_filter = ('process_description', 'uses_rectifier')
    search_fields = ('tank_number', 'process_description')
