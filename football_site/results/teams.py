from django.db import models 
from django.contrib import admin

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stadium = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True) 

    def __str__(self):
        return self.name
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', )