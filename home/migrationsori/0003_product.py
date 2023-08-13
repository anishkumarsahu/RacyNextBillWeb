# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-06-13 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_hsn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('brand', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('categoryID', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('mrp', models.FloatField(default=0.0)),
                ('cost', models.FloatField(default=0.0)),
                ('spWithoutGst', models.FloatField(default=0.0)),
                ('spWithGst', models.FloatField(default=0.0)),
                ('stock', models.IntegerField(default=0)),
                ('discountPc', models.FloatField(default=0.0)),
                ('barcode', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('status', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]