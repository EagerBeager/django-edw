# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-19 19:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edw', '0011_entity_description'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='entityrelation',
            unique_together=set([('term', 'from_entity', 'to_entity')]),
        ),
    ]