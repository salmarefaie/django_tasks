# Generated by Django 4.1.4 on 2023-01-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.TextField(default='default'),
        ),
    ]
