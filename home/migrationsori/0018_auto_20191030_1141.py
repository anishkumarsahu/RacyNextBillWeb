# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-10-30 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20191030_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categoryID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Category'),
        ),
    ]
