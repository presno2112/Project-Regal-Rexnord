from rest_framework import serializers
from RegalRexnord.models.results import Results
from RegalRexnord.models import User

class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk","first_name", "last_name", "email", "is_admin"] # por que no me deja seleccionar entre los usuarios?

class ResultsSerializer(serializers.ModelSerializer):
    user_data = UserSerializer2(read_only=True, source="user")
    class Meta:
        model = Results
        fields = "__all__"
        # como quitar el last login?


        # puedo hacer un serializer con información de otro modelo? EJ. leaderboard
