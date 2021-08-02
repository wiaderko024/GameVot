from django.urls import path
from .views import all_games, game_page


app_name = 'games'

urlpatterns = [
    path('all-games/', all_games, name='all_games'),
    path('<slug:game_slug>/', game_page, name='game_page'),
]
