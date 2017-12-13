from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pedidos/$', views.OrderPageView.as_view(), name='pedidos'),
    url(r'^novo-produto/$', views.CreateProduct.as_view(), name='novo-produto'),
    url(r'^(?P<title>[-\w]+)/(?P<pk>[0-9]+)/$', views.ProductView.as_view(), name='product-view'),
    url(r'^comment', views.AddCommentView.as_view(), name='add-comment'),
    url(r'^cozinhas', views.KitchensView.as_view(), name='cozinhas'),
    url(r'^cozinha/(?P<slug>[A-z]+)/$', views.CategoryView.as_view(), name='category'),
]