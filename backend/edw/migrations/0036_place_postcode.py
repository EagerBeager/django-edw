# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-10 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edw', '0035_auto_20161107_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='postcode',
            field=models.CharField(default='', max_length=16, verbose_name='Postcode'),
        ),
    ]
