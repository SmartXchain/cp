# rack/models.py

from django.db import models
from datetime import date


class Rack(models.Model):
    rack_number = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=100)
    application_type = models.CharField(max_length=100)
    last_inspection_date = models.DateField()
    next_inspection_date = models.DateField()
    inspection_frequency = models.CharField(max_length=50)  # e.g., "Weekly", "Monthly"
    condition = models.CharField(max_length=100)
    inspector = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="rack_photos/", blank=True, null=True)

    @property
    def is_overdue(self):
        return date.today() > self.next_inspection_date

    def __str__(self):
        return f"Rack {self.rack_number}"


class Inspection(models.Model):
    rack = models.ForeignKey(Rack, related_name="inspections", on_delete=models.CASCADE)
    inspection_date = models.DateField()
    inspector = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Inspection on {self.inspection_date} for Rack {self.rack.rack_number}"
