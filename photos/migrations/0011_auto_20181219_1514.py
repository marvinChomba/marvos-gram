# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 12:14
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_auto_20181219_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]