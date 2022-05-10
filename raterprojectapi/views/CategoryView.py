from unicodedata import category
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError

from raterprojectapi.models.category import Category

class CategoryView(ViewSet):
    """Rater game view"""
    
    def retrieve(self, request, pk):
        """Handle Get requests
        Returns:
            Response -- JSON serialized game
            """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response ({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle Get requests to get all games"""
        
        games = Category.objects.all()
        
        serializer = CategorySerializer(games, many=True)
        return Response(serializer.data)
    
class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    
    class Meta:
        model = Category
        fields = ('id','label')
