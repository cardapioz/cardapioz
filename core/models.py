# coding=utf-8


from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from localflavor import br
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    photo = ResizedImageField(size=[160, 160], quality=75, upload_to='user/profile', verbose_name='imagem', default='/imagens/img/user.svg')
    phone = models.CharField(max_length=11)
    sexo = models.BooleanField(choices=sexo, default=0)


class Adress(models.Model):
    user = models.ForeignKey(User)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=15)


class Store(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=60)
    photo = ResizedImageField(crop=[400, 400], default='/imagens/img/user.svg')
