# manual_method/models.py

from django.db import models


class ManualMethod(models.Model):
    PROCESS_CHOICES = [
        ("cleaning", "Cleaning"),
        ("pre_pen_etching", "Pre-Pen Etching"),
        ("rinsing", "Rinsing"),
        ("chrome_plating", "Chrome Plating"),
        ("cad_plating", "Cad Plating"),
        ("anodizing", "Anodizing"),
        ("nickel_plating", "Nickel Plating"),
        ("cad_strip", "Cad Strip"),
        ("chrome_strip", "Chrome Strip"),
        ("nickel_strip", "Nickel Strip"),
        ("passivation", "Passivation"),
        ("nital_etch", "Nital Etch"),
        ("deoxidizing", "Deoxidizing"),
    ]

    method_number = models.CharField(max_length=50, unique=True)
    description = models.TextField(help_text="Describe the manual method.")
    process_type = models.CharField(max_length=50, choices=PROCESS_CHOICES)
    temperature_min = models.FloatField(blank=True, null=True)
    temperature_max = models.FloatField(blank=True, null=True)
    time_immersion_min = models.FloatField(help_text="Minimum immersion time in minutes.", blank=True, null=True)
    time_immersion_max = models.FloatField(help_text="Maximum immersion time in minutes.", blank=True, null=True)
    test_required = models.CharField(max_length=100, blank=True, null=True, help_text="Specify test requirements, e.g., water break test.")

    def __str__(self):
        return f"Manual Method {self.method_number} - {self.get_process_type_display()}"
