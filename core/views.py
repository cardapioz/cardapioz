from allauth.account.views import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import FormView, UpdateView, DetailView, CreateView, ListView
from django.views.generic.base import TemplateView

#Models Import's
from core.forms import ProductForm, EditUser, CommentForm
from .models import Produto, Order, Comment, Category

# Rest Import's
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


# Class Based Views import's
from django.views import View
from django.views.generic.base import TemplateView


class OrderPageView(LoginRequiredMixin, TemplateView):
    template_name = 'core/orders.html'

    def get_context_data(self, **kwargs):
        context = super(OrderPageView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(client=self.request.user).exclude(delivered=1)
        context['orders_delivered'] = Order.objects.filter(client=self.request.user).exclude(delivered=0)
        return context


class HomeView(View):
    template = 'core/home.html'

    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all().order_by('-data_published')
        categorias = Category.objects.all().order_by('-data_create')[:6]
        return render(request, self.template, {'produtos': produtos, 'categorias': categorias})


class CategoryView(DetailView):
    model = Category
    template_name = 'core/category.html'

    def get_context_data(self, **kwargs):

        context = super(CategoryView, self).get_context_data(**kwargs)

        context['produtos'] = Produto.objects.filter(category_product__slug=self.kwargs.get('slug'))
        return context


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
            return render(request, 'core/user-edit.html', {'form': form})
    else:
        return render(request, 'core/user-edit.html', {'form': form})


class CreateProduct(LoginRequiredMixin, FormView):
    form_class = ProductForm
    template_name = 'core/create-product.html'
    success_url = '../'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.photo_thumb = self.request.FILES['photo_medium']

        return super(CreateProduct, self).form_valid(form.save())


class ProductView(DetailView):
    model = Produto
    template_name = 'core/product-view.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['produto'] = Produto.objects.get(pk=self.kwargs.get('pk'))
        context['comments'] = Comment.objects.filter(product=context['produto']).order_by('-data_create')
        context['comments_total'] = context['comments'].count()
        context['comments'] = context['comments'][:4]
        return context


class AddCommentView(View):
    form_class = CommentForm

    def post(self, request, *args):
        form = self.form_class(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = Produto.objects.get(pk=request.POST['product'])
            form.user = request.user
            form.save()
            return HttpResponse('Comentario cadastrado com sucesso!')
        else:
            return HttpResponse('Erro ao cadastrar comentario!', form.errors)


class KitchensView(ListView):
    model = Category
    template_name = 'core/kitchens.html'

    def get_context_data(self, **kwargs):
        context = super(KitchensView, self).get_context_data(**kwargs)
        return context