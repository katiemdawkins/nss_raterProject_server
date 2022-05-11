from django.db import models

class Game_Review(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="reviews")
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    
    