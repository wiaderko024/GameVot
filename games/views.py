from django.shortcuts import render
from .models import Game


def all_games(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'all_games.html', context=context)


def game_page(request, game_slug):
    game = Game.objects.get(slug=game_slug)

    context = {
        'game': game,
    }

    return render(request, 'game.html', context=context)
