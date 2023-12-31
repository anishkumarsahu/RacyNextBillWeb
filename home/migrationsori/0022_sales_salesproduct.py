# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-11-11 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20191111_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(blank=True, max_length=200, null=True)),
                ('customerGst', models.CharField(blank=True, max_length=200, null=True)),
                ('customerPhone', models.CharField(blank=True, max_length=200, null=True)),
                ('customerEmail', models.CharField(blank=True, max_length=200, null=True)),
                ('customerAddress', models.CharField(blank=True, max_length=500, null=True)),
                ('customerState', models.CharField(blank=True, max_length=200, null=True)),
                ('salesType', models.CharField(blank=True, max_length=200, null=True)),
                ('paymentType', models.CharField(blank=True, max_length=200, null=True)),
                ('creditDays', models.IntegerField(default=0)),
                ('invoiceNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('invoiceDate', models.DateField(blank=True, null=True)),
                ('subTotal', models.FloatField(default=0.0)),
                ('taxable', models.FloatField(default=0.0)),
                ('totalFinal', models.FloatField(default=0.0)),
                ('billDisc', models.FloatField(default=0.0)),
                ('gst', models.FloatField(default=0.0)),
                ('grandTotal', models.FloatField(default=0.0)),
                ('roundOff', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('customerID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='SalesProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('hsn', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('rate', models.FloatField(default=0.0)),
                ('gst', models.FloatField(default=0.0)),
                ('disc', models.FloatField(default=0.0)),
                ('netRate', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('productID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Product')),
                ('salesID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Sales')),
            ],
        ),
    ]
