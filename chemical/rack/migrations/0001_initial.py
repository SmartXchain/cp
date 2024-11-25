# Generated by Django 5.1.2 on 2024-10-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack_number', models.CharField(max_length=50, unique=True)),
                ('location', models.CharField(max_length=100)),
                ('last_inspection_date', models.DateField()),
                ('next_inspection_date', models.DateField()),
                ('inspection_frequency', models.CharField(max_length=50)),
                ('condition', models.CharField(max_length=100)),
                ('inspector', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='rack_photos/')),
            ],
        ),
    ]
