# Generated by Django 5.1.2 on 2024-11-28 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruction', '0002_instruction_parameters_instruction_process_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instruction',
            name='manual_method',
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='tank',
        ),
    ]
