from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    maker = models.CharField(max_length=40)
    yearReleased = models.IntegerField()
    numOfPlayers = models.IntegerField()
    estTimeToPlayMinutes = models.IntegerField()
    ageRec = models.IntegerField()
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)