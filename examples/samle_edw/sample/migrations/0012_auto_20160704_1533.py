# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0011_auto_20160629_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adultbook',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Fantastic'), (2, 'Drama'), (3, 'Mistics')], verbose_name='Genre'),
        ),
    ]