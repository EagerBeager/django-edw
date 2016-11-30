# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-11 13:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('edw', '0029_auto_20161007_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='MessageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField(default=0)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='message_images', to='filer.Image', verbose_name='Image')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edw.Message', verbose_name='Message')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Message image',
                'verbose_name_plural': 'Message images',
            },
        ),
        migrations.CreateModel(
            name='ParticularProblemMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='edw.Message', verbose_name='Message')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='edw.ParticularProblem', verbose_name='Particular problem')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.AlterField(
            model_name='datamart',
            name='terms',
            field=models.ManyToManyField(blank=True, related_name='_datamart_terms_+', to='edw.Term', verbose_name='Terms'),
        ),
        migrations.AddField(
            model_name='message',
            name='images',
            field=models.ManyToManyField(through='edw.MessageImage', to='filer.Image'),
        ),
        migrations.AddField(
            model_name='message',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edw.BasePerson', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='particularproblem',
            name='messages',
            field=models.ManyToManyField(blank=True, related_name='problem', through='edw.ParticularProblemMessage', to='edw.Message', verbose_name='Messages'),
        ),
    ]
