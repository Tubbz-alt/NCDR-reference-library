# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_schema', '0010_auto_20171103_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='row',
            name='data_dictionary_link',
        ),
        migrations.RemoveField(
            model_name='row',
            name='data_dictionary_name',
        ),
    ]
