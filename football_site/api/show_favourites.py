from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..results.favourite_games import FavouriteGame

@login_required  # This decorator ensures the user must be logged in
def favourite_games_view(request):
    # Fetch favorite games for the logged-in user, ordered by match date
    favourite_games = FavouriteGame.objects.filter(user=request.user).select_related('match', 'match__home_team', 'match__away_team').order_by('match__date')
    return render(request, 'results/favourite_games.html', {'favourite_games': favourite_games})

