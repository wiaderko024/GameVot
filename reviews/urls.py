from django.urls import path
from .views import rate_game


app_name = 'reviews'

urlpatterns = [
    path('rate/<int:game_id>/<int:rate>/', rate_game, name='rate_game'),
]
