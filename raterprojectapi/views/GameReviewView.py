from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from raterprojectapi.models.game import Game

from raterprojectapi.models.game_review import Game_Review
from raterprojectapi.models.gamer import Gamer

class GameReviewView(ViewSet):
    """Rater game view"""
    
    def retrieve(self, request, pk):
        """Handle Get requests
        Returns:
            Response -- JSON serialized game
            """
        try:
            game_review = Game_Review.objects.get(pk=pk)
            serializer = GameReviewSerializer(game_review)
            return Response(serializer.data)
        except Game_Review.DoesNotExist as ex:
            return Response ({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """Handle Get requests to get all games"""
        
        game_reviews = Game_Review.objects.all()
        
        serializer = GameReviewSerializer(game_reviews, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations"""
        
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])
        serializer = CreateGameReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(gamer=gamer, game=game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class GameReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    
    class Meta:
        model = Game_Review
        fields = ('id','game', 'gamer', 'content')
        depth = 1
        
class CreateGameReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    
    class Meta:
        model = Game_Review
        fields = ('id','game', 'gamer', 'content')
        depth = 1