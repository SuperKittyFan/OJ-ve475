# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attack', '0007_remove_attack_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='result',
            field=models.CharField(default='NONE', max_length=20),
        ),
    ]