# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 22:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20171220_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='end',
            new_name='deliver_on',
        ),
    ]