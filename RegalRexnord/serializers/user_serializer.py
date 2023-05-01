from rest_framework import serializers
from RegalRexnord.models import User

class DashboardSerializer(serializers.Serializer):
    pass

# solo funciona con .Serializer
class UserSerializer(serializers.ModelSerializer): #modelSerializer para enviar el id del usuario no el link

    totalscore = serializers.ReadOnlyField()
    avg_time = serializers.ReadOnlyField()
    games_completed = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {
            #"write_only": True, 
            "style":{"input_type":"password"}, 
            #"min-length" : "5" Hacer que la contraseña tenga mas de x caracteres

            }
        }

class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True,
        style={'input_type': 'password'}
    )
    email = serializers.EmailField(
        required=True
    )