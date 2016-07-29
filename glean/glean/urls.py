"""chatroom URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^base', login_required(TemplateView.as_view(template_name='base.html')), name='base'),
    url(r'^top', login_required(TemplateView.as_view(template_name='toppage.html')), name='top'),
    url(r'^login', 'django.contrib.auth.views.login', kwargs={'template_name': 'login.html'}, name='login'),
    url(r'^logout', 'django.contrib.auth.views.logout_then_login', kwargs={'login_url': 'login'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
]
