# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-24 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20171224_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='genre1',
            field=models.CharField(blank=True, choices=[('T', 'Türk'), ('Y', 'Yunan')], max_length=80),
        ),
    ]
