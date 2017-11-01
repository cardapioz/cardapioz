# Class Based Views import's
from django.views import View
from django.shortcuts import render, redirect
from product.models import Produto, Category
from allauth.account.views import logout


class HomeView(View):
    template = 'core/home.html'

    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all().order_by('-data_published')
        categorias = Category.objects.all().order_by('-data_create')[:6]
        return render(request, self.template, {'produtos': produtos, 'categorias': categorias})

