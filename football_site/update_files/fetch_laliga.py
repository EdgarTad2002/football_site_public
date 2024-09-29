
import requests
from bs4 import BeautifulSoup
from football_site.results.teams import Team
from football_site.results.matches import Match 
from django.http import HttpResponse


def la_liga_update():
    standings_url = 'https://fbref.com/en/comps/12/La-Liga-Stats'
    data = requests.get(standings_url)
    soup = BeautifulSoup(data.text, 'html.parser')

    # Find the table that contains team standings
    standings_table = soup.find('table', {'id': 'results2024-2025121_overall'})

    # Get all the rows of the standings table, skipping the header
    team_rows = standings_table.find_all('tr')[1:]

    # Loop through each row and extract relevant data
    for row in team_rows:
        team_name = row.find('td', {'data-stat': 'team'}).text.strip()
        games = row.find('td', {'data-stat': 'games'}).text.strip()
        wins = row.find('td', {'data-stat': 'wins'}).text.strip()
        draws = row.find('td', {'data-stat': 'ties'}).text.strip()
        losses = row.find('td', {'data-stat': 'losses'}).text.strip()
        goals_for = row.find('td', {'data-stat': 'goals_for'}).text.strip()
        goals_against = row.find('td', {'data-stat': 'goals_against'}).text.strip()
        goal_diff = row.find('td', {'data-stat': 'goal_diff'}).text.strip()
        points = row.find('td', {'data-stat': 'points'}).text.strip()

        team_logo_td = row.find('td', {'data-stat': 'team'})
        logo_img_tag = team_logo_td.find('img')
        logo_url = logo_img_tag['src']



        team, created = Team.objects.get_or_create(name=team_name)
        team.games = games 
        team.wins = wins
        team.draws = draws 
        team.losses = losses 
        team.goals_for = goals_for 
        team.goals_against = goals_against
        team.goal_diff = goal_diff
        team.points = points
        team.league = "La Liga"
        team.logo_url = logo_url

        team.save()

    
