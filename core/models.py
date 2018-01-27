# coding=utf-8
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from django_resized import ResizedImageField
from .choices import *
from star_ratings.models import Rating


class AbsPerm(models.Model):
    # For Staff
    is_active = models.BooleanField(_('Ativo na plataforma'), default=True)
    is_banned = models.BooleanField(_('Banido da plataforma'), default=False)
    data_create = models.DateTimeField(_('Criado em'), default=timezone.now)
    data_published = models.DateTimeField(_('Publicado em'), default=timezone.now)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='usuario')
    photo = ResizedImageField(size=[160, 160], quality=75, upload_to='user/profile', default='/imagens/img/user.svg',
                              blank=True, verbose_name='imagem',)
    phone = models.CharField(max_length=11, blank=True)
    sexo = models.BooleanField(choices=sexo, default=0)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'


class Address(models.Model):
    user = models.ForeignKey(User, related_name='address', blank=True, verbose_name='usuario')
    route = models.CharField(_('rua'), max_length=200)
    country = models.CharField(_('pais'), max_length=200)
    administrative_area_level_1 = models.CharField(_('estado'), max_length=200)
    administrative_area_level_2 = models.CharField(_('cidade'), max_length=200)
    street_number = models.CharField(_('número'), max_length=30)
    postal_code = models.CharField(_('CEP'), max_length=20)
    complement = models.CharField(_('complemento'), max_length=20)
    sublocality_level_1 = models.CharField(_('bairro'), max_length=200)

    def full_address(self):
        return f'{self.route}, {self.street_number} - {self.sublocality_level_1} -' \
               f' {self.administrative_area_level_2}'

    def __str__(self):
        return self.full_address


class Store(models.Model):
    owner = models.OneToOneField(User, related_name='store', blank=True)
    name = models.CharField(max_length=60, blank=True)
    photo = ResizedImageField(size=[400, 400], default='/imagens/img/user.svg', blank=True)
    adm = models.CharField(max_length=200, default=owner, blank=True)
