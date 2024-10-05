from django.urls import path
from rest_framework import routers
from .views import TeamViewSet,PlayerViewSet,GameViewSet,SeasonView




router = routers.DefaultRouter()
router.register(r'team', TeamViewSet,basename='team')
router.register(r'player',PlayerViewSet,basename='player')
router.register(r'game',GameViewSet,basename='game')
router.register(r'season',SeasonView,basename='season')
urlpatterns = router.urls
