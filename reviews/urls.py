from django.urls import path
from .views import rate_game, edit_review


app_name = 'reviews'

urlpatterns = [
    path('rate/<int:game_id>/<int:rate>/', rate_game, name='rate_game'),
    path('edit/<int:id>/', edit_review, name='edit_review'),
]
