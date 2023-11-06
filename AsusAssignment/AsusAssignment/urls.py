"""
URL configuration for AsusAssignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from main_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('how_it_works', views.how_it_works, name="how_it_works"),
    path('services', views.services, name="services"),
    path('contacts', views.contacts, name="contacts"),
    path('blog', views.blog, name="blog"),
    path('blog_details', views.blog_details, name="blog_details"),
    path('services_details', views.services_details, name="services_details"),
    path('faq', views.faq, name="faq"),
    path('legal', views.legal, name="legal"),
    path('t_c', views.t_c, name="t_c"),
    path('p_policy', views.p_policy, name="p_policy"),

    path("admin/", admin.site.urls),
]
