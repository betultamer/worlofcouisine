# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-24 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_food_top'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='genre1',
        ),
    ]
