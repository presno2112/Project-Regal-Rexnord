from rest_framework import serializers
from RegalRexnord.models.game import Game
from .results_serializer import ResultsSerializer


# que serializer usar? hyperlinked o serializer normal?
class GameSerializer(serializers.HyperlinkedModelSerializer): # cambiar a model Serializer para enviar a frontend
    results = ResultsSerializer(many=True, read_only=True)
    leaderboard = ResultsSerializer(many=True, read_only=True) # para mostrar la info relacionada (usuario y juego) se hace en front o back?
    class Meta:
        model = Game
        fields = "__all__"  

