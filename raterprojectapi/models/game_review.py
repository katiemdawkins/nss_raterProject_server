from django.db import models

class Game_Review(models.Model):
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamerId = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    content = models.CharField(max_length=150)