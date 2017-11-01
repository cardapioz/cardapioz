from django.conf.urls import url
from .views import CategoryApi

urlpatterns = [
    url(r'categorias/$', CategoryApi.as_view(), name='categoria-api'),
]