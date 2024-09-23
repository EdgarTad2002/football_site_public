import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.db import connection

from football_site.results.matches import Match
from football_site.results.teams import Team
from football_site.results.dataload import InitialDataLoad


def pl_fixtrues():

    if 'results_initialdataload' not in connection.introspection.table_names():
        print("InitialDataLoad table does not exist yet. Skipping fixtures loading.")
        return

    # Check if the data has already been loaded
    if InitialDataLoad.objects.filter(name='premier_league_fixtures', is_loaded=True).exists():
        print("Premier League fixtures have already been loaded.")
        return 

    standings_url = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'

    
    try:
        data = requests.get(standings_url)
        # data.raise_for_status()  # Raises an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    
    
    soup = BeautifulSoup(data.text, 'html.parser')

    # Find the table that contains team standings
    standings_table = soup.find('table', {'id': 'sched_2024-2025_9_1'})
    if not standings_table:
        print("Could not find standings table")
        return

    # Get all the rows of the standings table, skipping the header
    res = standings_table.find('tbody')
    rows = res.find_all('tr')
    final_rows = []

    for row in rows:
        # Skip rows that have the 'spacer' class or that don't have a valid gameweek (match day) value
        if 'spacer' in row.get('class', []) or 'thead' in row.get('class', []):
            continue

        match_date = row.find('td', {'data-stat': 'date'})
        match_time = row.find('td', {'data-stat': 'start_time'})
        datetime_str = f"{match_date.text} {match_time.text}".strip()
        match_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

        home_team = row.find('td', {'data-stat': 'home_team'}).text.strip()
        away_team = row.find('td', {'data-stat': 'away_team'}).text.strip()
        matchday = int(row.find('th', {'data-stat': 'gameweek'}).text.strip())
        score = row.find('td', {'data-stat': 'score'})

        if score and score.text.strip():
            score_text = score.text.strip()
            home_score, away_score = map(int, score_text.split('–'))
        else:
            home_score = None
            away_score = None

        home_team, created = Team.objects.get_or_create(name=home_team)
        away_team, created = Team.objects.get_or_create(name=away_team)

        match, created = Match.objects.update_or_create(
            date=match_datetime,
            home_team=home_team,
            away_team=away_team,
            defaults={
                'home_score': home_score,
                'away_score': away_score,
                'matchday': matchday,
            }
        )

        match.save()

        InitialDataLoad.objects.update_or_create(
            name = 'premier_league_fixtures',
            defaults={'is_loaded': True}
        )