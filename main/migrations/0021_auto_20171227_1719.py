# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20171227_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='genre',
            field=models.CharField(blank=True, choices=[('\xc7', '\xc7orbalar'), ('S', 'Salata'), ('T', 'Tatl\u0131'), ('A', 'At\u0131\u015ft\u0131rmal\u0131k'), ('Y', 'Yemek')], max_length=80),
        ),
    ]
