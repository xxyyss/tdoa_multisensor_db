# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('interface', '0012_auto_20170219_1059'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='softwarestate',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='softwarestate',
            name='computer',
        ),
        migrations.AddField(
            model_name='computer',
            name='is_active_sensor_controller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='computer',
            name='is_active_tdoa_controller',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='SoftwareState',
        ),
    ]
