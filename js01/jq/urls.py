"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

from jq import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='jq1.html'), name = 'jq1'),
    path('jq2',TemplateView.as_view(template_name='jq2.html'), name = 'jq2'),
    path('jq3',TemplateView.as_view(template_name='jq3.html'), name = 'jq3'),
    path('jq4',TemplateView.as_view(template_name='jq4.html'), name = 'jq4'),
    path('jq5',TemplateView.as_view(template_name='jq5.html'), name = 'jq5'),
    path('login',views.login, name = 'login'),
]
