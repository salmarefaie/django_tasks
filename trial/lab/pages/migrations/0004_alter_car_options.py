# Generated by Django 4.1.4 on 2023-01-04 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_car_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['name']},
        ),
    ]
