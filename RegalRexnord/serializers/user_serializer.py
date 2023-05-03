from rest_framework import serializers
from RegalRexnord.models import User, Results

class DashboardSerializer(serializers.ModelSerializer):
    #dashboard_info = serializers.ReadOnlyField()
    
    class Meta: 
        model = Results
        fields = ["attempt","score", "time", "completed"] # y si quiero meter propiedades de usuarios?

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
            #"write_only": True, por si no quiero que se acceda a la contraseña
            "style":{"input_type":"password"}, 

            },
            "last_login": {
            "read_only" : True    
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
