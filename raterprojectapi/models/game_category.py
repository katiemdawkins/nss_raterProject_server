from django.db import models

from raterprojectapi.models.category import Category   

class Game_Category(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)