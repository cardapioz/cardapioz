from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^login/$', views.login, name='user-login'),
    url(r'^logout/$', views.sair, name='sair'),
    url(r'^pedidos/$', views.orders, name='pedidos'),
    url(r'^perfil/$', views.user_edit, name='perfil'),
    url(r'^novo-produto/$', views.create_product, name='usuario'),
]
