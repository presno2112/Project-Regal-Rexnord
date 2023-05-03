from datetime import *
from django.utils import timezone
from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import action
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, status
from ..serializers.user_serializer import LoginSerializer, UserSerializer, DashboardSerializer
from RegalRexnord.models.user import User, UserManager
from RegalRexnord.models.results import Results
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
    authentication_classes = (SessionAuthentication, TokenAuthentication)

    @action (methods=["GET"], detail=False, serializer_class=LoginSerializer, permission_classes=[IsAuthenticated])
    def current_user(self, request):
        return Response({
            "user": str(request.user),
            "auth": str(request.auth)
        }, status=status.HTTP_200_OK) 

    @action (methods=["POST"], detail=False, serializer_class=LoginSerializer, permission_classes=[AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            try:
                user = User.objects.get(email=email) #select * from user where email=?, email
            except BaseException as e:
                raise ValidationError({"error": str(e)})

            if not check_password(password, user.password):
                raise ValidationError({"error": "Incorrect Password"})
            
            user.last_login = timezone.now() 
            user.save()
            print(user)
            token, created = Token.objects.get_or_create(user=user) # que hago con esto??
            print(token)

            return Response({"token":token.key}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    @action (methods=["GET"], detail=False, serializer_class=DashboardSerializer, permission_classes=[IsAuthenticated])
    def dashboard(self, request):
        serializer = DashboardSerializer(data=request.data)
        results = None
        if serializer.is_valid():
            user = User.objects.get(email=request.user)
            results = user.dashboard_info()
            print(results)
            response = DashboardSerializer(results, many=True, context={'request': request})
            return Response(response.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #Sign up
    
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        user = None
        if serializer.is_valid():
            user = User.objects.create_user(
                email = serializer.validated_data["email"], 
                password = serializer.validated_data["password"], 
                first_name = serializer.validated_data["first_name"], 
                last_name = serializer.validated_data["last_name"], 
                last_login = serializer.validated_data["last_login"],
                is_admin = serializer.validated_data["is_admin"]
            )
            user.save()
            response = UserSerializer(instance=user, context={'request': request} )

            return Response(response.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# regresar lista de usuarios

            
