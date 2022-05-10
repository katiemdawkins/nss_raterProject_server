from django.db import models   
    
class Game_Pics(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    picture=models.CharField(max_length=500)