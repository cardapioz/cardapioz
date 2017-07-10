import re

from django.utils import timezone

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField



class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('O nome de usuário deve ser fornecido'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


choicesexo = ((0, 'Masculino'), (1, 'Feminino'))


class UserBussiness(models.Model):
    company_name = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)


class User(AbstractBaseUser, PermissionsMixin, UserBussiness):
    def get_short_name(self):
        pass

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    # user data
    first_name = models.CharField(_('nome'), max_length=30)
    last_name = models.CharField(_('sobrenome'), max_length=30)

    locale = models.CharField(max_length=200, default='')
    gender = models.CharField(max_length=40, default='')
    email = models.EmailField(_('email'), max_length=255, unique=True,
                              error_messages=dict(unique="este email já está em uso."))
    username = models.CharField(_('username'), max_length=30, blank=True, null=True, unique=True,
                                error_messages={'unique': "este nome de usuario já esta em uso"},
                                help_text=_('Não pode conter caracteres especiais.'), validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Digite um nome valido.'), _('invalid'))])
    sexo = models.BooleanField(choices=choicesexo, default=0)

    user_photo = ResizedImageField(size=[160, 160], quality=75, upload_to='users_photos', blank=True,
                                   default='core/img/user.png')
    user_photos = ResizedImageField(size=[160, 160], quality=75, upload_to='users_photos', blank=True)

    # system data
    date_joined = models.DateTimeField(_('Data de criação'), default=timezone.now)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_("Define se é admin."))
    is_active = models.BooleanField(_('Email ativado'), default=True, help_text=_("Define se o usuario está ativo."))
    is_pass = models.BooleanField(_('Cadastrou senha? '), default=False, help_text='Possui senha')
    is_trusty = models.BooleanField(_('Conta Ativa'), default=False, help_text=_("Define se a conta é ativada."))
    type_user = models.BooleanField(_('empresa'), default=False, help_text=_('define se é empresa ou usuario normal'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class UserAddress(models.Model):
    user = models.ForeignKey('User', related_name='user_address')
    address = models.CharField(max_length=200)

