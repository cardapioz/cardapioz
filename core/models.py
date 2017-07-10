# coding=utf-8
import sys
import time

from PIL import Image

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField

from .choices import *

#image1 = ResizedImageField(size=[600, 600], upload_to='whatever')
# image2 = ResizedImageField(size=[100, 100], crop=['top', 'left'], upload_to='whatever')
# image3 = ResizedImageField(size=[100, 100], crop=['middle', 'center'], upload_to='whatever')
# image4 = ResizedImageField(size=[500, 300], quality=75, upload_to='whatever')


class AbsPerm(models.Model):
    # For Staff
    is_active = models.BooleanField(_('Ativo na plataforma'), default=True)
    is_banned = models.BooleanField(_('Banido da plataforma'), default=False)
    data_create = models.DateTimeField(default=timezone.now)
    data_published = models.DateTimeField(default=timezone.now)


class Ingredient(models.Model):
    word = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=False)

    def __unicode__(self):
        return self.word

    def __str__(self):
        return self.word.capitalize()


class ProductSize(models.Model):
    sizes = models.CharField(max_length=18)

    def __str__(self):
        return self.sizes


class Category(AbsPerm, models.Model):
    title = models.CharField(max_length=30, unique=True, blank=False)
    category_photo = ResizedImageField(size=[390, 200], crop=['top', 'left'], quality=100, upload_to='category')
    description = models.TextField(max_length=144)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Produto(AbsPerm, models.Model):
    owner = models.ForeignKey('accounts.User', related_name='owner')
    title = models.CharField(default='', max_length=30, blank=False, null=False)
    description = models.TextField(default='', max_length=300)
    category_product = models.ForeignKey('Category', related_name='categorias')
    amount = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    preparation_time = models.IntegerField(default=0)
    sizes = models.ManyToManyField('ProductSize')
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients')

    photo_thumb = ResizedImageField(size=[250, 250], crop=['top', 'left'], quality=75,
                                    upload_to='products_photos/thumb', blank=True)
    photo_medium = ResizedImageField(size=[700, 510], crop=['top', 'left'], quality=90, upload_to='products_photos/medium')

    def __str__(self):
        return self.title

    def category_title(self):
        return self.category_product.title

    def save(self, **kwargs):
        super(Produto, self).save()

        if self.data_create is None:
            self.data_create = timezone.now()

        self.data_published = timezone.now()

        super(Produto, self).save()


class Order(AbsPerm, models.Model):
    product = models.ForeignKey('Produto', related_name='produto')
    client = models.ForeignKey('accounts.User', related_name='cliente')
    amount = models.IntegerField(default=1)

    value = models.IntegerField(default=0)

    payment = models.IntegerField(choices=payment_methods, default=0)

    delivered = models.BooleanField(default=0)
    status = models.IntegerField(choices=status_order, default=0)

    def get_status(self):
        return status_order[self.status][1]

    def __str__(self):
        return 'Pedido de: {} Item: {}'.format(self.client.get_full_name(), self.product.title)

    def save(self, **kwargs):
        super(Order, self).save()
        self.value = self.product.price * self.amount
        super(Order, self).save()


class Comment(AbsPerm, models.Model):
    product = models.ForeignKey('Produto', related_name='product_comment')
    user = models.ForeignKey('accounts.User', related_name='usuario')
    comment_text = models.TextField(max_length=144)

    def __str__(self):
        return self.comment_text[0:30] + '...'
