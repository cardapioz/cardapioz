# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-22 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20171221_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='orders',
            field=models.ManyToManyField(related_name='pedido', to='product.Order'),
        ),
    ]