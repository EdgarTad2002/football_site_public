from django.shortcuts import render
from ..results.matches import Match
from ..results.teams import Team

def home(request):
    premier_league_results = Match.objects.filter(home_team__league='Premier League', home_score__isnull=False, away_score__isnull=False).order_by('-date')[:5]
    la_liga_results = Match.objects.filter(home_team__league='La Liga', home_score__isnull=False, away_score__isnull=False).order_by('-date')[:5]
    
    premier_league_fixtures = Match.objects.filter(home_team__league='Premier League', home_score__isnull=True, away_score__isnull=True).order_by('date')[:5]
    la_liga_fixtures = Match.objects.filter(home_team__league='La Liga', home_score__isnull=True, away_score__isnull=True).order_by('date')[:5]

    premier_league_table = Team.objects.filter(league="Premier League").order_by('-points', '-goal_diff')[:3]
    la_liga_table = Team.objects.filter(league="La Liga").order_by('-points', '-goal_diff')[:3]

    context = {
        'premier_league_results': premier_league_results,
        'la_liga_results': la_liga_results,
        'premier_league_fixtures': premier_league_fixtures,
        'la_liga_fixtures': la_liga_fixtures,
        'premier_league_table': premier_league_table,
        'la_liga_table': la_liga_table,
    }
    return render(request, 'results/home.html', context)

