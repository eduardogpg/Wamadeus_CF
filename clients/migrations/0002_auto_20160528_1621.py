# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='bio',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='job',
            field=models.CharField(max_length=50),
        ),
    ]
