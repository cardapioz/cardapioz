# Class Based Views import's
from django.views import View
from django.shortcuts import render

from product.models import Produto, Category


class HomeView(View):
    template = 'core/home.html'

    def get(self, request):
        produtos = Produto.objects.all()
        produtos = {'lasted': produtos.order_by('-data_published'),
                    'highest_rating': produtos.order_by('-ratings__average')}

        categorias = Category.objects.all().order_by('-data_create')[:6]
        return render(request, self.template, {'title': 'Experiencia', 'produtos': produtos, 'categorias': categorias})

