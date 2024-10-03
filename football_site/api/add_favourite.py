from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..results.favourite_games import FavouriteGame
from ..results.matches import Match
from django.db import IntegrityError

@login_required
def add_favourite_game(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    
    # Check if the match is already a favorite for the user
    favorite, created = FavouriteGame.objects.get_or_create(user=request.user, match=match)

    if not created:  # If it already exists, it means we want to remove it
        favorite.delete()

    return redirect(request.META.get('HTTP_REFERER', 'premier-league'))
