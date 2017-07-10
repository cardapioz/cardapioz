from django.shortcuts import render

# Create your views here.
from django.views.generic import UpdateView

from accounts import User


class UserEdit(UpdateView):
    model = User
    fields = ['user_photo', 'first_name', 'last_name']
    template_name_suffix = 'edit-user'