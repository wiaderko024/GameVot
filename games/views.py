from django.shortcuts import render
from .models import Game
from categories.models import Category


def all_games(request):
    games = Game.objects.all()
    categories = Category.objects.all()

    context = {
        'games': games,
        'categories': categories,
    }

    return render(request, 'all_games.html', context=context)


def game_page(request, game_slug):
    game = Game.objects.get(slug=game_slug)
    categories = Category.objects.all()

    context = {
        'game': game,
        'categories': categories,
    }

    return render(request, 'game.html', context=context)
