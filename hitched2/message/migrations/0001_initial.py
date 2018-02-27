# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-27 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('otherParty', models.CharField(max_length=13)),
                ('fromMe', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('isMedia', models.BooleanField(default=False)),
                ('mediaName', models.TextField(default=None)),
            ],
        ),
    ]
