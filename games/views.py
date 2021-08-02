from django.shortcuts import render
from .models import Game


def all_games(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'all_games.html', context=context)
