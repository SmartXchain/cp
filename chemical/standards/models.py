# standards/models.py

from django.db import models
from instruction.models import Instruction


class Standard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    revision = models.CharField(max_length=20)
    author = models.CharField(max_length=100)
    class_field = models.CharField(max_length=50, default="I")  # Use `class_field` to avoid conflict with Python's `class`
    type = models.CharField(max_length=50)
    process = models.TextField()  # Instructions for processing a part

    def __str__(self):
        return self.name


class Inspection(models.Model):
    standard = models.ForeignKey(Standard, related_name='inspections', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    acceptance_criteria = models.TextField()
    paragraph_section = models.CharField(max_length=50)
    sampling_plan = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.standard.name}"


class ProcessStep(models.Model):
    standard = models.ForeignKey(Standard, related_name="process_steps", on_delete=models.CASCADE)
    step_number = models.PositiveIntegerField()
    instruction = models.ForeignKey(Instruction, on_delete=models.SET_NULL, null=True)
    operator = models.CharField(max_length=100)
    date = models.CharField(max_length=50)  # Store date as text

    def __str__(self):
        return f"Step {self.step_number} for {self.standard.name}"
