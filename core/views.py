from allauth.account.views import logout
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.base import TemplateView

#Models Import's
from core.forms import ProductForm, EditUser
from .models import Produto, Order

# Rest Import's
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


def home(request):
    produto = Produto.objects.all().order_by('-data_published')
    return render(request, 'core/home.html', {'produtos': produto})


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
    orders = Order.objects.filter(client=request.user)
    orders_delivered = orders.exclude(delivered=0)
    orders = orders.exclude(delivered=1)

    return render(request, 'core/orders.html', {'orders': orders, 'orders_delivered': orders_delivered})


def user_edit(request):
    form = EditUser(instance=request.user)
    if request.method == 'POST':
        form = EditUser(request.POST, instance=request.user)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_photo = request.FILES['user_photo']
            form.save()
            return redirect('perfil')
        else:
            print(form.errors)
            return render(request, 'core/user-edit.html', {'form': form})
    else:
        return render(request, 'core/user-edit.html', {'form': form})


def create_product(request):
    form_post = ProductForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        if form_post.is_valid():
            form_post = form_post.save(commit=False)

            form_post.photo_medium = request.FILES['photo_medium']
            form_post.photo_thumb = request.FILES['photo_medium']
            form_post.author = request.user

            form_post.save()

            return redirect('index')
        else:
            print(form_post.errors)
            return render(request, 'core/create-product.html', {'error': 'erro ao criar produto', 'form': form_post})
    else:
        return render(request, 'core/create-product.html', {'form': form_post})