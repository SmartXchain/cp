# standards/models.py

from django.db import models
from instruction.models import Instruction


class Standard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    revision = models.CharField(max_length=20)
    author = models.CharField(max_length=100)
    # Files will be stored in MEDIA_ROOT/uploads/
    standard_file = models.FileField(upload_to='files/', blank=True)
    def __str__(self):
        return self.name

class Classification(models.Model):
    classification = models.ForeignKey(Standard, related_name='classification', on_delete=models.CASCADE)
    classes = models.CharField(max_length=50)
    types = models.CharField(max_length=50)
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_three = models.CharField(max_length=50)

class Inspection(models.Model):
    standard = models.ForeignKey(Standard, related_name='inspections', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    acceptance_criteria = models.TextField()
    paragraph_section = models.CharField(max_length=50)
    sampling_plan = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.standard.name}"
