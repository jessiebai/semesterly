# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-07 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0002_auto_20170520_1927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agreement',
            options={'get_latest_by': 'last_updated'},
        ),
    ]
