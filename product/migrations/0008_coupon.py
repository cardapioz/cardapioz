# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20171218_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Cupom',
                'verbose_name_plural': 'Cupons',
            },
        ),
    ]
