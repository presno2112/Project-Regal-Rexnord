from rest_framework import serializers
from RegalRexnord.models.results import Results
from RegalRexnord.models import User

class UserSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"] # por que no me deja seleccionar entre los usuarios?

class ResultsSerializer(serializers.HyperlinkedModelSerializer):
    #user = UserSerializer2()
    class Meta:
        model = Results
        fields = "__all__"
        # como quitar el last login?


        # puedo hacer un serializer con información de otro modelo? EJ. leaderboard
