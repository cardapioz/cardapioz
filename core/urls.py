from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^login/$', views.login, name='user-login'),
    url(r'^logout/$', views.sair, name='sair'),
    url(r'^pedidos/$', views.orders, name='pedidos')
]
