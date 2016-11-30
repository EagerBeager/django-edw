# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-19 19:06
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('edw', '0012_auto_20160919_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='state',
            field=django_fsm.FSMField(default='new', max_length=50),
        ),
    ]
