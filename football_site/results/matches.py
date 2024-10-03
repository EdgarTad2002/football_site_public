from django.db import models
from django.contrib import admin
from .teams import Team
from django.contrib.auth.models import User

class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateTimeField()
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)
    matchday = models.IntegerField(null=True)

    

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'date', 'home_score', 'away_score')
    list_filter = ('date', 'home_team', 'away_team')
    search_fields = ('home_team__name', 'away_team__name')
    ordering = ('-date',)


    
