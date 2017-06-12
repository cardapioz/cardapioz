from allauth.account.views import logout
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView

# Rest Import's
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


def home(request):
    posts = ''
    return render(request, 'core/home.html', {'posts': posts})


def login(request):
    if not request.user.is_authenticated:
        return render(request, 'core/login.html')
    else:
        return redirect('index')


def sair(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    else:
        return redirect('login')


def orders(request):
    return render(request, 'core/orders.html', {'forms': 'a'})