from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests

from football_site.results.teams import Team 
from football_site.results.matches import Match

def update_laliga_fixtures():
    standings_url = 'https://fbref.com/en/comps/12/schedule/La-Liga-Scores-and-Fixtures'

    try:
        data = requests.get(standings_url)
        # data.raise_for_status()  # Raises an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    
    
    soup = BeautifulSoup(data.text, 'html.parser')

    # Find the table that contains team standings
    standings_table = soup.find('table', {'id': 'sched_2024-2025_12_1'})
    if not standings_table:
        print("Could not find standings table")
        return

    # Get all the rows of the standings table, skipping the header
    res = standings_table.find('tbody')
    rows = res.find_all('tr')

    today = datetime.now()
    previous_day = today - timedelta(days=2)
    next_day = today + timedelta(days=2)

    for row in rows:
        # Skip rows that have the 'spacer' class or that don't have a valid gameweek (match day) value
        if 'spacer' in row.get('class', []) or 'thead' in row.get('class', []):
            continue

        match_date = row.find('td', {'data-stat': 'date'})
        match_time = row.find('td', {'data-stat': 'start_time'})
        datetime_str = f"{match_date.text} {match_time.text}".strip()
        match_datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

        if not (previous_day <= match_datetime <= next_day):
            continue

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
