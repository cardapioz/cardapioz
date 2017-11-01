# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 05:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_loggedinuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='absperm_ptr',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='absperm_ptr',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='loggedinuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='absperm_ptr',
        ),
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='absperm_ptr',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='category_product',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='sizes',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='LoggedInUser',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
