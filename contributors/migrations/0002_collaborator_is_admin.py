# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborator',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]