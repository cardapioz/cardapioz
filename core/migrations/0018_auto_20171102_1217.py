# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20171101_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absperm',
            name='data_create',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='absperm',
            name='data_published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publicado em'),
        ),
    ]
