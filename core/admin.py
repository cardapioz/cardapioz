from django.contrib import admin
from .models import AbsPerm, Profile, Adress, Store
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.


class PerfilEdit(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Dado de usuarios'
    verbose_name = 'Dado de usuario'


class AddressUser(admin.StackedInline):
    model = Adress
    can_delete = False
    extra = 0
    verbose_name = 'Endereço do usuário'
    verbose_name_plural = 'Endereços do usuário'


class SotreUser(admin.StackedInline):
    model = Store
    can_delete = False
    verbose_name_plural = 'Empresas'
    verbose_name = 'Empresa'


class UserAdmin(BaseUserAdmin):
    inlines = (PerfilEdit, AddressUser, SotreUser)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(AbsPerm)
