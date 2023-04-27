from datetime import timezone
from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import action
from rest_framework import viewsets, status
from ..serializers.game_serializer import GameSerializer
from ..models.game import Game
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class GameView(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]
    authentication_classes = (SessionAuthentication, TokenAuthentication)

# Hacer accion de leaderboard
# post desde unity?
# ayuda para conectar con react
# acordar con karla qué vamos a mostrar
