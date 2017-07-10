from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^login/$', views.login, name='user-login'),
    url(r'^logout/$', views.sair, name='sair'),
    url(r'^pedidos/$', views.OrderPageView.as_view(), name='pedidos'),
    url(r'^novo-produto/$', views.CreateProduct.as_view(), name='usuario'),
    url(r'^(?P<title>[-\w]+)/p=(?P<pk>[0-9])/$', views.ProductView.as_view(), name='product-view'),
    url(r'^', include('accounts.urls')),
    url(r'^comment', views.AddCommentView.as_view(), name='add-comment'),
    url(r'^cozinhas', views.KitchensView.as_view(), name='cozinhas'),

    url(r'^(?P<slug>[A-z]+)/$', views.CategoryView.as_view(), name='category'),
]
