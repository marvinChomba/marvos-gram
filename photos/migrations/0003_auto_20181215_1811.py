# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-15 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20181215_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Hey there', max_length=40),
        ),
    ]
