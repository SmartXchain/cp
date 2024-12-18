# Generated by Django 5.1.2 on 2024-11-06 15:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruction',
            name='parameters',
            field=models.TextField(blank=True, help_text='Recordable items/parameters for this instruction'),
        ),
        migrations.AddField(
            model_name='instruction',
            name='process_category',
            field=models.CharField(choices=[('Masking', 'Masking'), ('Abrasive Blasting', 'Abrasive Blasting'), ('Electroplating', 'Electroplating'), ('Anodizing', 'Anodizing')], default=django.utils.timezone.now, help_text='Select the process category', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instruction',
            name='custom_description',
            field=models.TextField(blank=True, help_text='Additional custom instructions', null=True),
        ),
    ]
