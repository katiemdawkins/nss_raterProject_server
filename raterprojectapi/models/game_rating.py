from django.db import models

class Game_Rating(models.Model):
    #we can access the relationship here between game and ratings
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="ratings")
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    rating = models.IntegerField()
    
    
