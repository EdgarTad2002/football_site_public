from django.db import models
from django.contrib import admin

class InitialDataLoad(models.Model):    
    name = models.CharField(max_length=50, unique=True)
    is_loaded = models.BooleanField(default=False)

@admin.register(InitialDataLoad)
class InitialDataLoadAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_loaded')

