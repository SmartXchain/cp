# Generated by Django 5.1.2 on 2024-11-06 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manual_method', '0001_initial'),
        ('tank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('custom_description', models.TextField(blank=True, help_text='Optional: Add any custom instructions.', null=True)),
                ('manual_method', models.ForeignKey(blank=True, help_text='Optional: Link to a manual method.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='manual_method.manualmethod')),
                ('tank', models.ForeignKey(blank=True, help_text='Optional: Link to a tank.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tank.tank')),
            ],
        ),
    ]
