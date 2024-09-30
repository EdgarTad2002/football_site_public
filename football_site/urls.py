"""
URL configuration for football_site project.

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

from .api import home_view, pl_views, laliga_views, teams

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.home, name='home'),
    path('premier-league/', pl_views.premier_league, name='premier_league'),
    path('la-liga/', laliga_views.la_liga, name='la_liga'),
    path('team/<int:team_id>/', teams.team_detail, name='team_detail'),
    #path('run/', pl.viewpl, name='viewpl')
]
