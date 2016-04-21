# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vampire', '0004_auto_20160420_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('brid', models.AutoField(primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=20)),
                ('blood_group', models.CharField(choices=[(0, 'Select'), (1, 'A+'), (2, 'A-'), (3, 'B+'), (4, 'B-'), (5, 'AB+'), (6, 'AB-'), (7, 'O+'), (8, 'O+'), (9, 'O-'), (10, 'A1+'), (11, 'A1-'), (12, 'A2+'), (13, 'A2-'), (14, 'A1B+'), (15, 'A1B-'), (16, 'A2B+'), (17, 'A2B-'), (18, 'Bombay Blood')], default=0, max_length=2)),
                ('patient_age', models.PositiveIntegerField()),
                ('requirement_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('units', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hospital_name', models.CharField(max_length=20)),
                ('purpose', models.TextField(max_length=200)),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vampire.Address')),
            ],
        ),
        migrations.RemoveField(
            model_name='bloodsample',
            name='bbid',
        ),
        migrations.RemoveField(
            model_name='bloodsample',
            name='did',
        ),
        migrations.RemoveField(
            model_name='reserves',
            name='bsid',
        ),
        migrations.RemoveField(
            model_name='reserves',
            name='hid',
        ),
        migrations.RemoveField(
            model_name='bloodbank',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='bloodbank',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='blood_type',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='longitude',
        ),
        migrations.AddField(
            model_name='bloodbank',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='bloodbank',
            name='username',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='donor',
            name='blood_group',
            field=models.CharField(choices=[(0, 'Select'), (1, 'A+'), (2, 'A-'), (3, 'B+'), (4, 'B-'), (5, 'AB+'), (6, 'AB-'), (7, 'O+'), (8, 'O+'), (9, 'O-'), (10, 'A1+'), (11, 'A1-'), (12, 'A2+'), (13, 'A2-'), (14, 'A1B+'), (15, 'A1B-'), (16, 'A2B+'), (17, 'A2B-'), (18, 'Bombay Blood')], default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='donor',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='BloodSample',
        ),
        migrations.DeleteModel(
            name='Reserves',
        ),
    ]
