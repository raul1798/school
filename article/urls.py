"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from article import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^history/$', TemplateView.as_view(template_name="history.html"), name='history'),
    url(r'^novosti/$', views.novosti, name='novosti'),
    url(r'^novosti/get/(?P<article_pk>[0-9]+)/$', views.novost, name='novost'),
    url(r'^resursy/', TemplateView.as_view(template_name="interes.html"), name='interes'),
    url(r'^base/', TemplateView.as_view(template_name="base.html"), name='base'),
    url(r'^porady/', TemplateView.as_view(template_name="porady.html"), name='porady'),
    url(r'^vpravy/', TemplateView.as_view(template_name="vpravy.html"), name='vpravy'),
    url(r'^photo/', TemplateView.as_view(template_name="photo.html"), name='photo'),
    url(r'^contact/', TemplateView.as_view(template_name="karta.html"), name='karta'),
    url(r'^dpa/$', views.dpa, name='dpa'),
    url(r'^zno/$', views.zno, name='zno'),
    url(r'^klassam/$', views.klassam, name='klassam'),
    url(r'^vchitel/$', views.vchitel, name='vchitel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    )