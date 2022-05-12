from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from raterprojectapi.models.game import Game

from raterprojectapi.models.game_rating import Game_Rating
from raterprojectapi.models.gamer import Gamer

class GRatingView(ViewSet):
    """Rater game view"""
    
    def retrieve(self, request, pk):
        """Handle Get requests
        Returns:
            Response -- JSON serialized game
            """
        try:
            game_rating = Game_Rating.objects.get(pk=pk)
            serializer = RatingSerializer(game_rating)
            return Response(serializer.data)
        except Game_Rating.DoesNotExist as ex:
            return Response ({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle Get requests to get all games"""
        
        game_ratings = Game_Rating.objects.all()
        
        serializer = RatingSerializer(game_ratings, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations"""
        
        game= Game.objects.get(pk=request.data['game'])
        gamer = Gamer.objects.get(user=request.auth.user)
        serializer = CreateRatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer, game=game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    
    class Meta:
        model = Game_Rating
        fields = ('id','game', 'gamer', 'rating')
        depth=1
        
class CreateRatingSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    
    class Meta:
        model = Game_Rating
        fields = ('id','game', 'gamer', 'rating')
        depth=1