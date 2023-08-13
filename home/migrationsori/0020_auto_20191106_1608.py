# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-11-06 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20191030_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('hsn', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('rate', models.FloatField(default=0.0)),
                ('gst', models.FloatField(default=0.0)),
                ('netRate', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('productID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Product')),
            ],
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='name',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='price',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='supplier_Id',
        ),
        migrations.AddField(
            model_name='purchase',
            name='creditDays',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='gst',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='invoiceDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='invoiceNumber',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchase',
            name='paymentType',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchaseType',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplierAddress',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplierEmail',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplierGst',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplierID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Supplier'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplierName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplierPhone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplierState',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='taxable',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='purchaseproduct',
            name='purchaseID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Purchase'),
        ),
    ]