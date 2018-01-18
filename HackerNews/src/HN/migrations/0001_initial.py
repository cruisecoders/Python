# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hnews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hn_id', models.IntegerField(default=0, null=True, unique=True)),
                ('username', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('url', models.CharField(max_length=300, null=True)),
                ('score', models.CharField(max_length=150, null=True)),
                ('hn_type', models.CharField(max_length=150, null=True)),
                ('sentiments', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
