# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-10-10 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_companyprofile_isdeleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyuser',
            name='city',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='state',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='zip',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
