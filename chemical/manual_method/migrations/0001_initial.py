# Generated by Django 5.1.2 on 2024-10-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManualMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_number', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(help_text='Describe the manual method.')),
                ('process_type', models.CharField(choices=[('cleaning', 'Cleaning'), ('pre_pen_etching', 'Pre-Pen Etching'), ('rinsing', 'Rinsing'), ('chrome_plating', 'Chrome Plating'), ('cad_plating', 'Cad Plating'), ('anodizing', 'Anodizing'), ('nickel_plating', 'Nickel Plating'), ('cad_strip', 'Cad Strip'), ('chrome_strip', 'Chrome Strip'), ('nickel_strip', 'Nickel Strip'), ('passivation', 'Passivation'), ('nital_etch', 'Nital Etch'), ('deoxidizing', 'Deoxidizing')], max_length=50)),
                ('temperature_min', models.FloatField(blank=True, null=True)),
                ('temperature_max', models.FloatField(blank=True, null=True)),
                ('time_immersion_min', models.FloatField(blank=True, help_text='Minimum immersion time in minutes.', null=True)),
                ('time_immersion_max', models.FloatField(blank=True, help_text='Maximum immersion time in minutes.', null=True)),
                ('test_required', models.CharField(blank=True, help_text='Specify test requirements, e.g., water break test.', max_length=100, null=True)),
            ],
        ),
    ]