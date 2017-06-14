from django.contrib import admin
from .models import UserBusiness, User, MyModel
# Register your models here.

admin.site.register(UserBusiness)
admin.site.register(User)
admin.site.register(MyModel)