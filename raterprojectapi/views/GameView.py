from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError

from raterprojectapi.models.game import Game
from raterprojectapi.models.gamer import Gamer
from raterprojectapi.views.GameRatingView import RatingSerializer
from raterprojectapi.views.GameReviewView import GameReviewSerializer

class GameView(ViewSet):
    """Rater game view"""
    
    def retrieve(self, request, pk):
        """Handle Get requests
        Returns:
            Response -- JSON serialized game
            """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response ({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle Get requests to get all games"""
        
        games = Game.objects.all()
        
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations"""
        
        gamer = Gamer.objects.get(user=request.auth.user)
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """handle PUT requests"""
        
        game = Game.objects.get(pk=pk)
        serializer= CreateGameSerializer(game, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
            
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    #we have reviews because of the related name in GameReview model
    #the serializer gives us back what we want
    reviews = GameReviewSerializer(many=True)
    #ratings = RatingSerializer(many=True)
    
    class Meta:
        model = Game
        fields = ('id','title', 'description', 'maker', 'year_released', 'num_of_players', 'est_time_to_play_minutes', 'age_rec', 'gamer', 'categories', 'reviews', 'average_rating')
        depth = 1

class CreateGameSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    
    class Meta:
        model = Game
        fields = ('id','title', 'description', 'maker', 'year_released', 'num_of_players', 'est_time_to_play_minutes', 'age_rec', 'gamer', 'categories')
        depth = 1