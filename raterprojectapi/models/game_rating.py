from django.db import models

class Game_Rating(models.Model):
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    rating = models.IntegerField()