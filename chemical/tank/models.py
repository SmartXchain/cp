# tank/models.py

from django.db import models


class Tank(models.Model):
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

    tank_number = models.CharField(max_length=50, unique=True)
    components_makeup = models.TextField(help_text="List all components used for tank makeup.")
    temperature_min = models.FloatField()
    temperature_max = models.FloatField()
    uses_rectifier = models.BooleanField(default=False)
    rectifier_number = models.CharField(max_length=50, blank=True, null=True)
    time_immersion_min = models.FloatField(help_text="Minimum immersion time in minutes.")
    time_immersion_max = models.FloatField(help_text="Maximum immersion time in minutes.")
    test_required = models.CharField(max_length=100, blank=True, null=True, help_text="Specify test requirements, e.g., water break test.")
    process_description = models.CharField(max_length=50, choices=PROCESS_CHOICES)

    def __str__(self):
        return f"Tank {self.tank_number} - {self.get_process_description_display()}"
