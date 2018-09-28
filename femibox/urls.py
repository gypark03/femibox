"""femibox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from femibox.views import AboutView, HomeView
from accounts.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),

    url(r'^question/', include('question.urls', namespace='question')),
    url(r'^femiLetter/', include('femiLetter.urls', namespace='femiLetter')),
    url(r'^notice/',include('notice.urls', namespace='notice')),
    url(r'^product/',include('product.urls', namespace='product')),
    url(r'^campaign/',include('campaign.urls', namespace='campaign')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
