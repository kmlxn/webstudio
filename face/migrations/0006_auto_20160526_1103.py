# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0005_auto_20160526_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='snippet',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='snippet_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='snippet_ru',
            field=models.TextField(null=True),
        ),
    ]
