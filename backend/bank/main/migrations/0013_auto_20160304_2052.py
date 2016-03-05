# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20160304_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default='5774637528129', unique=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='trans_type',
            field=models.CharField(choices=[('Withdraw', 'Withdraw'), ('Deposit', 'Deposit')], max_length=10),
        ),
    ]