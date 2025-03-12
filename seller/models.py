from django.db import models

class Handler(models.Model):
    Warenname = models.CharField(max_length=50)
    Beschreibung = models.CharField(max_length=150)
    Preis = models.CharField(max_length=10, blank=True)

