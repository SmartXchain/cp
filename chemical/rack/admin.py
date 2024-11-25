# rack/admin.py

from django.contrib import admin
from .models import Rack, Inspection


@admin.register(Rack)
class RackAdmin(admin.ModelAdmin):
    list_display = ('rack_number', 'location', 'last_inspection_date', 'next_inspection_date', 'condition', 'inspector')


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ('rack', 'inspection_date', 'inspector', 'condition')
