# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-10-12 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_companyuser_isdeleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wareHouseName', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('wareHouseAddress', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]