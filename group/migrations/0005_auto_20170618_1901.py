# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_auto_20170618_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='cipher',
            field=models.TextField(default='Nonparticipator'),
        ),
    ]