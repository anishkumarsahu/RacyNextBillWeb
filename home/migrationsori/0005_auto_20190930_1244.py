# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-09-30 12:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_sales_salesproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('accNo', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('branch', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('accountType', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('ifsc', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('bankAddress', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('email', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('userPassword', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('supplier_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('return_amount', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('salesID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Sales')),
            ],
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='bank_detail',
        ),
        migrations.AddField(
            model_name='companyuser',
            name='company_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='user_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankdetails',
            name='companyID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile'),
        ),
    ]
