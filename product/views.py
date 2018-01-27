from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse , HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import TemplateView , DetailView , ListView , FormView , UpdateView
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.serializer import CommentSerializer , OrderSerializer , CartSerializer , AddressSerializer
from .forms import CommentForm, ProductForm
from .models import Produto , Order , Comment , Category , Cart


class OrderPageView(LoginRequiredMixin, TemplateView):
    template_name = 'product/orders.html'

    def get_context_data(self, **kwargs):
        context = super(OrderPageView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(client=self.request.user).exclude(delivered=1).order_by('-data_published')
        context['orders_delivered'] = Order.objects.filter(client=self.request.user).exclude(delivered=0)
        return context


class CategoryView(DetailView):
    model = Category
    template_name = 'product/category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.filter(category_product__slug=self.kwargs.get('slug'))
        return context


class ProductView(DetailView):
    model = Produto
    template_name = 'product/product-view.html'

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
    template_name = 'product/product-list.html'

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
    template_name = 'product/kitchens.html'
    template_name_suffix = 'Cozinhas'
    paginate_by = 12
    ordering = 'slug'


class CreateProduct(LoginRequiredMixin, FormView):
    form_class = ProductForm
    template_name = 'product/create-product.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.photo_thumb = self.request.FILES['photo_medium']

        return super(CreateProduct, self).form_valid(form.save())


class ProdutoEdit(UpdateView):
    model = Produto
    form_class = ProductForm
    template_name = 'product/create-product.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        try:
            obj.photo_thumb = self.request.FILES['photo_medium']
        except Exception as e:
            print(e)

        return super(ProdutoEdit, self).form_valid(form.save())

    def dispatch(self, request, *args, **kwargs):
        produto = self.get_object()
        if produto.owner != self.request.user:
            return redirect('meus-produtos')
        return super(ProdutoEdit, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        get_produto = Produto.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('product-view', kwargs={'title': slugify(get_produto.title), 'pk': get_produto.pk})


class CommentApi(APIView):
    serializer_class = CommentSerializer

    def get(self, request, pk):
        serializer = self.serializer_class(Comment.objects.filter(product=pk).order_by('-data_published')[:4], many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self):
        return Response(status=status.HTTP_200_OK)


class OrderView(APIView):
    serializer_class = OrderSerializer
    #permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = self.serializer_class(Order.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class CartView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'product/cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['list_cart'] = self.model.objects.filter(user=self.request.user).exclude(status=1).last()
        return context


class CartApi(APIView):
    serializer_class = CartSerializer

    def get(self, request):
        serializer = self.serializer_class(Cart.objects.filter(user=request.user), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        order_id = request.data['order_id']
        cart = Cart.objects.filter(user=request.user).exclude(status=1).last()
        cart.orders.remove(order_id)
        serializer = self.serializer_class(data=cart)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, pk):
        serializer = self.serializer_class(Order.objects.get(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        Response(status=status.HTTP_200_OK)


class AddressView(APIView):
    serializer_class = AddressSerializer
    #permission_classes = [permissions.IsAuthenticated,]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)