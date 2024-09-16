from django.db import models 
from django.contrib import admin

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # stadium = models.CharField(max_length=100, blank=True, null=True)
    # logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    games = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    draws = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    goals_for = models.IntegerField(null=True)
    goals_against = models.IntegerField(null=True)
    goal_diff = models.IntegerField(null=True)
    points = models.IntegerField(null=True)

    def __str__(self):
        return self.name 
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', )