from django.contrib.auth.models import AbstractUser, User
from core.models import Profile
from product.models import Comment
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