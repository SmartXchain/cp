# standards/admin.py

from django.contrib import admin
from .models import Standard, Inspection, ProcessStep


@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('name', 'revision', 'author')


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'standard', 'paragraph_section')


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('standard', 'step_number', 'instruction')
