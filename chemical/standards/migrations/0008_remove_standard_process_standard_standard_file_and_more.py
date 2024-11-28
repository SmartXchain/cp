# Generated by Django 5.1.2 on 2024-11-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standards', '0007_remove_standard_class_field_remove_standard_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standard',
            name='process',
        ),
        migrations.AddField(
            model_name='standard',
            name='standard_file',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
        migrations.DeleteModel(
            name='ProcessStep',
        ),
    ]
