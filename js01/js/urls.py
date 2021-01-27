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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='home.html'), name = 'home'),
    path('js1',TemplateView.as_view(template_name='js1.html'), name = 'js1'),
    path('js2',TemplateView.as_view(template_name='js2.html'), name = 'js2'),
    path('js3',TemplateView.as_view(template_name='js3.html'), name = 'js3'),
    path('js4',TemplateView.as_view(template_name='js4.html'), name = 'js4'),
    path('js5',TemplateView.as_view(template_name='js5.html'), name = 'js5'),
    path('js6',TemplateView.as_view(template_name='js6.html'), name = 'js6'),
    path('js7',TemplateView.as_view(template_name='js7.html'), name = 'js7'),
    path('js8',TemplateView.as_view(template_name='js8.html'), name = 'js8'),
    path('js9',TemplateView.as_view(template_name='js9.html'), name = 'js9'),
    path('js10',TemplateView.as_view(template_name='js10.html'), name = 'js10'),
]
