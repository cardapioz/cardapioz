from django.contrib import admin
from .models import UserBusiness, User, MyModel, Ingredient, Produto, ProductSize, Order
# Register your models here.

admin.site.register(UserBusiness)
admin.site.register(User)
admin.site.register(MyModel)
admin.site.register(Ingredient)
admin.site.register(Produto)
admin.site.register(ProductSize)
admin.site.register(Order)