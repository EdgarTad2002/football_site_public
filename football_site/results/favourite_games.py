from django.contrib.auth.models import User
from django.db import models
from .models import Match
from django.contrib import admin

class FavouriteGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'match')

    def __str__(self):
        return f"{self.user.username}'s favorite match: {self.match}"
    
@admin.register(FavouriteGame)
class FavouriteGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'match')
