# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-11-13 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20191113_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='paidDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='paidDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
