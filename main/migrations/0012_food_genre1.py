# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-23 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20171224_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='genre1',
            field=models.CharField(blank=True, choices=[('T', 'Türk'), ('İ', 'İtalyan'), ('Y', 'Yunan')], max_length=80),
        ),
    ]
