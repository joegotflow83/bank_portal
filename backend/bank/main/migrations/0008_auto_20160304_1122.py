# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160304_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='account_num',
        ),
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.IntegerField(default='5892372638423'),
        ),
    ]