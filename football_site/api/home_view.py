from django.shortcuts import render
from ..results.matches import Match
from ..results.teams import Team


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def home(request):
    last_pl_game = Match.objects.filter(home_team__league='Premier League', home_score__isnull=False, away_score__isnull=False).order_by('-date')[0]
    last_laliga_game = Match.objects.filter(home_team__league='La Liga', home_score__isnull=False, away_score__isnull=False).order_by('-date')[0]

    pl_matchday, laliga_matchday = last_pl_game.matchday, last_laliga_game.matchday

    premier_league_results = Match.objects.filter(home_team__league='Premier League', matchday=pl_matchday)
    la_liga_results = Match.objects.filter(home_team__league='La Liga', matchday=laliga_matchday)
    
    premier_league_fixtures = Match.objects.filter(home_team__league='Premier League', matchday=pl_matchday+1)
    la_liga_fixtures = Match.objects.filter(home_team__league='La Liga', matchday=laliga_matchday+1)

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


def login_view(request):
    from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Correctly calling login() with both request and user
            next_url = request.POST.get('next', '/')  # Use POST data for next
            return redirect(next_url)
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')



