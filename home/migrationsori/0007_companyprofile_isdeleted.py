# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-10-01 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190930_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
    ]