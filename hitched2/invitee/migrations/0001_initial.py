# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-27 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=13)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]
