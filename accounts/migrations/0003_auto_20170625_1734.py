# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 20:34
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170625_1556'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('user', django.db.models.manager.Manager()),
            ],
        ),
    ]
