from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^perfil/(?P<pk>[0-9])/$', views.UserEdit.as_view(), name='perfil'),
]