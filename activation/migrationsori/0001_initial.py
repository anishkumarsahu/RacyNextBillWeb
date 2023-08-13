# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-12-21 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Validity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activationDate', models.DateField(null=True)),
                ('expiryDate', models.DateField(null=True)),
                ('activationType', models.CharField(blank=True, max_length=100, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
