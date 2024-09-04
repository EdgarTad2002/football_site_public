from django.shortcuts import render, get_object_or_404
from ..results.teams import Team
from ..results.matches import Match

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team_fixtures = Match.objects.filter(home_team=team) | Match.objects.filter(away_team=team)
    team_fixtures = team_fixtures.order_by('date')  # Order by date
    
    context = {
        'team': team,
        'team_fixtures': team_fixtures,
    }
    
    return render(request, 'results/team_detail.html', context)
