from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    maker = models.CharField(max_length=40)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    est_time_to_play_minutes = models.IntegerField()
    age_rec = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)