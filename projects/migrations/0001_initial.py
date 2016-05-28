# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 16:50
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=200)),
                ('create_at', models.DateField(default=datetime.datetime.now)),
                ('dead_line', models.DateField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=100)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Status'),
        ),
    ]
