from rest_framework import serializers
from product.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        depth = 1
        fields = ['title', 'category_photo']