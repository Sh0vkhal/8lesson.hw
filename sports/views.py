from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.
from .models import Team,Player,Game,Season
from .serializers import TeamSerializer,PlayerSerializer,GameSerializer,SeasonSerializer



class TeamViewSet(ModelViewSet):
    queryset =Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = [TokenAuthentication]


class PlayerViewSet(ModelViewSet):
    queryset =Player.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = [TokenAuthentication]


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer



class SeasonView(ModelViewSet):   
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer 
