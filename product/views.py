from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, FormView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.serializer import CommentSerializer
from .forms import CommentForm, ProductForm
from .models import Produto, Order, Comment, Category


class OrderPageView(LoginRequiredMixin, TemplateView):
    template_name = 'core/orders.html'

    def get_context_data(self, **kwargs):
        context = super(OrderPageView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(client=self.request.user).exclude(delivered=1)
        context['orders_delivered'] = Order.objects.filter(client=self.request.user).exclude(delivered=0)
        return context


class CategoryView(DetailView):
    model = Category
    template_name = 'core/category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.filter(category_product__slug=self.kwargs.get('slug'))
        return context


class ProductView(DetailView):
    model = Produto
    template_name = 'core/product-view.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['produto'] = Produto.objects.get(pk=self.kwargs.get('pk'))
        context['relateds'] = Produto.objects.filter(category_product=context['produto'].category_product).exclude(pk=context['produto'].pk)[:6]
        context['comments'] = Comment.objects.filter(product=context['produto']).order_by('-data_create')
        context['comments_total'] = context['comments'].count()
        context['comments'] = context['comments'][:4]

        return context


class ProductList(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'core/product-list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['list_products'] = self.model.objects.filter(owner=self.request.user)
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
    template_name_suffix = 'Cozinhas'
    paginate_by = 12
    ordering = 'slug'

    '''def get_context_data(self, **kwargs):
        context = super(KitchensView, self).get_context_data(**kwargs)
        context['category_list'] = context['category_list'].order_by('slug')
        context['title'] = 'cozinha'
        return context
    '''


class CreateProduct(LoginRequiredMixin, FormView):
    form_class = ProductForm
    template_name = 'core/create-product.html'
    success_url = '../'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.photo_thumb = self.request.FILES['photo_medium']

        return super(CreateProduct, self).form_valid(form.save())


class CommentApi(APIView):
    serializer_class = CommentSerializer

    def get(self, request, pk):
        serializer = self.serializer_class(Comment.objects.filter(product=pk).order_by('-data_published')[:4], many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        return Response(status=status.HTTP_200_OK)