# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-11-11 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20191106_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasereturn',
            name='salesID',
        ),
        migrations.RemoveField(
            model_name='salesproduct',
            name='salesID',
        ),
        migrations.DeleteModel(
            name='PurchaseReturn',
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
        migrations.DeleteModel(
            name='SalesProduct',
        ),
    ]