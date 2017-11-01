"""cardapioz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django_private_chat import urls as django_private_chat_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'', include('product.urls')),
    url(r'^api/', include('api.urls')),
    url(r'sobre/', include('about.urls')),
    url(r'^', include('django_private_chat.urls')),
    url(r'^accounts/', include('allauth.urls'))
]


admin.site.site_title, admin.site.site_header = 'Cardapioz', 'Cardapioz'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
