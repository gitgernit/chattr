# Generated by Django 5.0.4 on 2024-04-23 20:08

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='max_time',
            field=models.IntegerField(default=1440, verbose_name='MaxTime'),
        ),
        migrations.AlterField(
            model_name='room',
            name='max_users',
            field=models.IntegerField(default=24, verbose_name='MaxUsers'),
        ),
    ]
