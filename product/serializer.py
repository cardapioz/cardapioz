from django.contrib.auth.models import AbstractUser, User
from core.models import Profile , Address
from product.models import Comment , Order , Cart
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        depth = 1
        fields = ['id', 'get_full_name']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    data_published = serializers.DateTimeField(format='%D %H:%m')

    class Meta:
        model = Comment
        depth = 0
        fields = ['id', 'product', 'comment_text', 'user', 'data_published']


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        depth = 0
        fields = ['user', 'city', 'state', 'address', 'number', 'postal_code']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        depth = 0
        fields = ['id', 'product', 'client', 'deliver_on', 'note', 'amount', 'payment']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        depth = 0
        fields = ['id', 'orders', 'status']