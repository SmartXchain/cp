# instruction/admin.py

from django.contrib import admin
from .models import Instruction

@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ('title', 'process_category', 'parameters')
    readonly_fields = ('parameters',)  # Make parameters read-only in admin
