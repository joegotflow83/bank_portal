# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160303_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='account_number',
            new_name='account_num',
        ),
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default='4221910739175'),
        ),
    ]
