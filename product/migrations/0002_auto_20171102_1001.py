# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 12:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsize',
            name='sizes',
        ),
        migrations.AddField(
            model_name='productsize',
            name='size',
            field=models.CharField(default=1, max_length=18, verbose_name='Tamanho'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category_photo',
            field=django_resized.forms.ResizedImageField(crop=['top', 'left'], keep_meta=True, quality=100, size=[390, 200], upload_to='category', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=144, verbose_name='Descricão'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=30, unique=True, verbose_name='Titulo Categoria'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='Em estoque'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='category_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='product.Category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='description',
            field=models.TextField(default='', max_length=300, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredients', to='product.Ingredient', verbose_name='Ingredientes'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Criador'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preparation_time',
            field=models.IntegerField(default=0, help_text='Em minutos', verbose_name='Tempo de preparo'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='price',
            field=models.FloatField(default=0, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='sizes',
            field=models.ManyToManyField(related_name='sizes', to='product.ProductSize', verbose_name='Tamanhos'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='title',
            field=models.CharField(default='', max_length=30, verbose_name='Titulo'),
        ),
    ]
