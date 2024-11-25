# instruction/models.py

from django.db import models

class ProcessCategory(models.TextChoices):
    MASKING = 'Masking', 'Masking'
    ABRASIVE_BLASTING = 'Abrasive Blasting', 'Abrasive Blasting'
    ELECTROPLATING = 'Electroplating', 'Electroplating'
    ANODIZING = 'Anodizing', 'Anodizing'
    # Additional categories as needed

# Define a dictionary of default parameters for each category
CATEGORY_PARAMETERS = {
    ProcessCategory.MASKING: "Masking family",
    ProcessCategory.ABRASIVE_BLASTING: "Media, Pressure, Offset distance",
    ProcessCategory.ELECTROPLATING: "Strike voltage, Plating voltage, Temperature, Current",
    ProcessCategory.ANODIZING: "Voltage, Current density, Solution temperature",
    # Continue with other categories and their parameters
}

class Instruction(models.Model):
    title = models.CharField(max_length=200)
    
    process_category = models.CharField(
        max_length=50,
        choices=ProcessCategory.choices,
        help_text="Select the process category"
    )
    
    parameters = models.TextField(blank=True, help_text="Recordable items/parameters for this instruction")
    custom_description = models.TextField(blank=True, null=True, help_text="Additional custom instructions")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-fill parameters based on the selected process category
        if self.process_category and not self.parameters:
            self.parameters = CATEGORY_PARAMETERS.get(self.process_category, "")
        super().save(*args, **kwargs)

