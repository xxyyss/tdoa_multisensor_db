# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('interface', '0002_sensor_heartbeat_interval'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='radius',
            field=models.FloatField(default=150),
        ),
    ]
