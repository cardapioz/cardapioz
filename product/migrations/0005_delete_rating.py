# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 21:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20171102_1217'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
