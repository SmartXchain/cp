# Generated by Django 5.1.2 on 2024-10-29 19:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards', '0004_alter_processstep_time_in_alter_processstep_time_out_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processstep',
            old_name='description',
            new_name='instructions',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='manual_step_number',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='operator_signoff',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='soak_temperature',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='tank_number',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='time_in',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='time_out',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='title',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='work_instruction',
        ),
        migrations.AddField(
            model_name='processstep',
            name='date',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processstep',
            name='operator',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
