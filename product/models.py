from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from django_resized import ResizedImageField
from star_ratings.models import Rating

from core.choices import payment_methods, status_order
from core.models import AbsPerm, Address

# Create your models here.


class Ingredient(models.Model):
    word = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=False)

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    def __unicode__(self):
        return self.word

    def __str__(self):
        return self.word.capitalize()


class ProductSize(models.Model):
    size = models.CharField(_('Tamanho'), max_length=18)

    class Meta:
        verbose_name = 'Tamanho de produto'
        verbose_name_plural = 'Tamanhos de produto'

    def __str__(self):
        return self.size


class Category(AbsPerm, models.Model):
    title = models.CharField(_('Titulo Categoria'), max_length=30, unique=True, blank=False)
    category_photo = ResizedImageField(_('Imagem'), size=[390, 200], crop=['top', 'left'], quality=100,
                                       upload_to='category')
    description = models.TextField(_('Descrição'), max_length=144)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.title.capitalize()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Coupon(models.Model):
    code = models.CharField(_('Código'), max_length=30, unique=True, blank=True,)

    class Meta:
        verbose_name = 'Cupom'
        verbose_name_plural = 'Cupons'


class Produto(AbsPerm, models.Model):
    owner = models.ForeignKey('auth.User', related_name='owner', verbose_name='Criador')
    title = models.CharField(_('Titulo'), default='', max_length=30, blank=False, null=False)
    description = models.TextField(_('Descrição'), max_length=300)
    category_product = models.ForeignKey('Category', related_name='categorias', verbose_name='Categoria')
    amount = models.IntegerField(_('Em estoque'), default=1)
    price = models.FloatField(_('Preço'), default=0)
    preparation_time = models.IntegerField(_('Tempo de preparo'), help_text='Em minutos', default=0)
    sizes = models.ManyToManyField('ProductSize', verbose_name='Tamanhos')
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients', verbose_name='Ingredientes')

    photo_medium = ResizedImageField(_('Imagem Média'), help_text='600x600', size=[700, 510], crop=['top', 'left'],
                                     quality=90, upload_to='products_photos/medium')
    photo_thumb = ResizedImageField(_('Imagem Thumb'), help_text='250x250', size=[250, 250], crop=['top', 'left'],
                                    quality=75, upload_to='products_photos/thumb', blank=True)

    ratings = GenericRelation(Rating, related_query_name='high_products')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.title

    def category_title(self):
        return self.category_product.title

    def save(self, **kwargs):
        super(Produto, self).save()

        if self.data_create is None:
            self.data_create = timezone.now()

        self.data_published = timezone.now()

        super(Produto, self).save()


class Order(AbsPerm, models.Model):
    product = models.ForeignKey('Produto', related_name='produto', verbose_name='produto', blank=False)
    deliver_on = models.ForeignKey('core.Address', related_name='endereco', verbose_name='entregar em', blank=False)
    client = models.ForeignKey('auth.User', related_name='cliente', verbose_name='cliente', blank=False)
    amount = models.IntegerField(default=1, verbose_name='quantidade', blank=False, null=False)
    note = models.TextField(max_length=500, verbose_name='observação', blank=True, null=True)
    value = models.IntegerField(default=0, verbose_name='valor', blank=True)
    payment = models.IntegerField(choices=payment_methods, default=0, verbose_name='forma de pagamento')
    status = models.IntegerField(choices=status_order, default=0, verbose_name='andamento')
    delivered = models.BooleanField(default=0, verbose_name='entregue', blank=True)
    must_orders = GenericRelation(Produto, related_query_name='must_orders', blank=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def get_status(self):
        return status_order[self.status][1]

    def get_info(self):
        return f'Quantidade: {self.amount}, Produto: {self.product.title} R${self.value}'

    def __str__(self):
        return f'Pedido de: {self.client.get_full_name()} Item: {self.product.title}'

    def save(self, **kwargs):
        super(Order, self).save()
        self.value = self.product.price * self.amount
        super(Order, self).save()


class Comment(AbsPerm, models.Model):
    product = models.ForeignKey('Produto', related_name='product_comment', verbose_name='produto')
    user = models.ForeignKey(User, related_name='usuario', verbose_name='usuario')
    comment_text = models.TextField(_('cometário'), max_length=144)

    class Meta:
        verbose_name = _('Cometário')
        verbose_name_plural = 'Cometários'

    def __str__(self):
        return f'{self.comment_text[0:30]}...'


class Cart(AbsPerm, models.Model):
    orders = models.ManyToManyField('Order', related_name='pedido', verbose_name='pedidos')
    user = models.ForeignKey(User, related_name='usuario_pedido', verbose_name='comprador')
    status = models.BooleanField(default=0, choices=((0, 'Na espera'), (1, 'Finalizado')))
    value_cart = models.FloatField(default=0, verbose_name='valor do carrinho')

    class Meta:
        verbose_name = _('carrinho')
        verbose_name_plural = _('carrinhos')

    def __str__(self):
        return f'Carrinho de compras de {self.user.get_full_name()} com: {self.orders.count()} produtos'
