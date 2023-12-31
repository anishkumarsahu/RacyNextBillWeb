# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-10-22 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_warehouse_isdeleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdetails',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customer',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hsn',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='supplier',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
