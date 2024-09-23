from django.db import models

class InitialDataLoad(models.Model):    
    name = models.CharField(max_length=50, unique=True)
    is_loaded = models.BooleanField(default=False)

