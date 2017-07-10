from django.contrib import admin
from .models import Ingredient, Produto, ProductSize, Order, AbsPerm, Comment, Category
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(AbsPerm)
admin.site.register(Produto)
admin.site.register(ProductSize)
admin.site.register(Order)
admin.site.register(Category)


class _Commment(admin.ModelAdmin):
    list_display = ['__str__', 'product', 'user', 'is_active', 'is_banned']

admin.site.register(Comment, _Commment)