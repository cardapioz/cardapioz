# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 00:22
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171027_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfiluser',
            name='user_photo',
        ),
        migrations.AddField(
            model_name='perfiluser',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=None, default='/static/core/img/user.png', keep_meta=True, quality=75, size=[200, 200], upload_to='user/profile', verbose_name='imagem'),
        ),
    ]
