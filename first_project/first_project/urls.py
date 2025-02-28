"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from home.views import *
from second_app.views import *
from third_app.views import *
from django_temp.views import *
urlpatterns = [

    path('',home,name = "home"),
    path("admin/", admin.site.urls),
    path("test/",test,name='test'),
    path("basic/",basic,name='basic'),
    path("second",second,name='second'),
    path("third",third,name='third'),
    path("templates",templates,name='templates')
]

