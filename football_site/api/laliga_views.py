from itertools import groupby
from django.shortcuts import render
from ..results.teams import Team
from ..results.matches import Match
from ..results.favourite_games import FavouriteGame


def la_liga(request):

    la_liga_table = Team.objects.filter(league="La Liga").order_by('-points', '-goal_diff', '-goals_for')
    la_liga_fixtures = Match.objects.filter(home_team__league="La Liga").order_by('matchday', 'date')
    if request.user.is_authenticated:
        user_favourites = FavouriteGame.objects.filter(user=request.user).values_list('match_id', flat=True)
    else:
        user_favourites = []

    fixtures_by_matchweek = {}
    for matchday, matches in groupby(la_liga_fixtures, key=lambda x: x.matchday):
        fixtures_by_matchweek[matchday] = list(matches)

    context = {
        'la_liga_table': la_liga_table,
        'fixtures_by_matchweek': fixtures_by_matchweek,
        'user_favourites': user_favourites,
    }

    return render(request, 'results/la_liga.html', context) 