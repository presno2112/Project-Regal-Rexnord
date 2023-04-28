from datetime import timezone
from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from ..serializers.results_serializer import ResultsSerializer
from ..models.results import Results

class ResultsView(viewsets.ModelViewSet):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [AllowAny] # cambiar despues de probar
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    
    