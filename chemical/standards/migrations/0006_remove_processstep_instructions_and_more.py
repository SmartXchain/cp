# Generated by Django 5.1.2 on 2024-11-06 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruction', '0001_initial'),
        ('standards', '0005_rename_description_processstep_instructions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processstep',
            name='instructions',
        ),
        migrations.AddField(
            model_name='processstep',
            name='instruction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instruction.instruction'),
        ),
    ]
