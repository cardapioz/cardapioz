from django.conf.urls import url
from .views import AboutView
urlpatterns = [
    url(r'cardapioz', AboutView.as_view(), name='about')
]