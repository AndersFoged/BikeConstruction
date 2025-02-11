"""
URL configuration for BikeConstructionDjango project.

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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include, re_path
# from AlbumsApp import views as albums_views
from HomeApp import views as first_views


def case_insensitive(url_pattern):
    ignored_case_regex = ''.join([f'[{c.upper()}|{c.lower()}]' for c in url_pattern])
    return f'{ignored_case_regex}'

urlpatterns = [
    # path('', albums_views.home),
    #path('admin/', admin.site.urls),
    path('', include('HomeApp.urls')),
    path('home/', include('HomeApp.urls')),
    path('', include('BikesApp.urls')),
    path('bikes/', include('BikesApp.urls')), 
    path('components/', include('ComponentsApp.urls')),
    #re_path(f"{case_insensitive('Albums/')}", include('AlbumsApp.urls'))

    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
