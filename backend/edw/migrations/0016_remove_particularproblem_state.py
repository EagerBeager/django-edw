# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-20 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edw', '0015_auto_20160919_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='particularproblem',
            name='state',
        ),
    ]
