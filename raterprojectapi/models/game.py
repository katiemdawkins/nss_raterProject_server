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
    categories = models.ManyToManyField("Category", through="Game_Category", related_name="games")
    
    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = self.ratings.all()

        # Sum all of the ratings for the game
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating

        # Calculate the averge and return it.
        ave_rating = total_rating / len(ratings)
        return ave_rating
        
        #return the result