# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 13:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attack', '0004_auto_20170618_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attack',
            old_name='akey',
            new_name='key',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='aresult',
            new_name='result',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='atext',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='awhom',
            new_name='whom',
        ),
    ]
