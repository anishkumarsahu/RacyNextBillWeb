# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-12-20 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_expense_expensetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='brand',
            field=models.CharField(blank=True, default='N/A', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
