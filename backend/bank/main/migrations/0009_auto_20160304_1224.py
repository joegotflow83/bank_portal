# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160304_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='current_balance',
            field=models.DecimalField(decimal_places=2, default=200.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default='7596634896210'),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
