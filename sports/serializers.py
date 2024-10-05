from rest_framework import serializers

from .models import Team,Player,Game,Season


class TeamSerializer(serializers.Serializer):
    class Meta:
        model = Team
        fields = '__all__'



class PlayerSerializer(serializers.Serializer):
    class Meta:
        model = Player
        fields = '__all__'



class GameSerializer(serializers.Serializer):
    class Meta:
        model = Game
        fields = '__all__'



class SeasonSerializer(serializers.Serializer):
    class Meta:
        model = Season
        fields = '__all__'      
          