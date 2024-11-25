# Generated by Django 5.1.2 on 2024-10-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards', '0003_processstep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='time_in',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='processstep',
            name='time_out',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='processstep',
            name='work_instruction',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
