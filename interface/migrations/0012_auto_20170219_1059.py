# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('interface', '0011_auto_20170217_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='failure_probability',
            field=models.FloatField(default=0.0001),
        ),
    ]
