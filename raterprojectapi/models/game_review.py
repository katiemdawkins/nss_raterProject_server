from django.db import models

class Game_Review(models.Model):
    #game is the 1 relatedName is the many. its acting as an added property on the game model
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="reviews")
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    
    