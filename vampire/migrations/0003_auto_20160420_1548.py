# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vampire', '0002_auto_20160419_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='donor',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
    ]