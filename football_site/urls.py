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
from django.urls import path, re_path
from django.views.generic import RedirectView

from .api import home_view, pl_views, laliga_views, teams, add_favourite, login_view, logout_view, show_favourites, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.home, name='home'),
    path('premier-league/', pl_views.premier_league, name='premier_league'),
    path('la-liga/', laliga_views.la_liga, name='la_liga'),
    path('team/<int:team_id>/', teams.team_detail, name='team_detail'),
    path('login/', login_view.CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view.custom_logout, name='logout'),
    path('match/<int:match_id>/favourite', add_favourite.add_favourite_game, name='mark_favourite'),
    path('favourite-games/', show_favourites.favourite_games_view, name="favourite_games"),
    path('sign-up/', signup_view.sign_up, name='sign-up'),

    re_path(r'^accounts/login/$', RedirectView.as_view(url='/login/')),
    #path('run/', pl.viewpl, name='viewpl')
]
