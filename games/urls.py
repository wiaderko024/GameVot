from django.urls import path
from .views import all_games


app_name = 'games'

urlpatterns = [
    path('all-games/', all_games, name='all_games'),
]
