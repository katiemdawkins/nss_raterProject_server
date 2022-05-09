from django.db import models

from raterprojectapi.models.category import Category   

class Game_Category(models.Model):
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)
    categoryId = models.ForeignKey("Category", on_delete=models.CASCADE)