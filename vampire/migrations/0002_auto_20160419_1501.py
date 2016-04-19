# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vampire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='password',
            field=models.CharField(default='0000', max_length=200),
        ),
        migrations.AddField(
            model_name='donor',
            name='username',
            field=models.CharField(default='#', max_length=200),
        ),
        migrations.AddField(
            model_name='hospital',
            name='password',
            field=models.CharField(default='0000', max_length=200),
        ),
        migrations.AddField(
            model_name='hospital',
            name='username',
            field=models.CharField(default='#', max_length=200),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='donor',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]