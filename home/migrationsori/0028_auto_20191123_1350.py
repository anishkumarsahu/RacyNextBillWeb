# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-11-23 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20191120_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='addedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.CompanyUser'),
        ),
        migrations.AddField(
            model_name='sales',
            name='companyID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile'),
        ),
    ]
