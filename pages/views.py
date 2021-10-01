from django.shortcuts import render
from categories.models import Category
from games.models import Game


def home_page(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'index.html', context=context)


def rankings_page(request):
    categories = Category.objects.all()

    games = Game.objects.all().order_by('avg_rate').reverse()
    best_games = []

    for i in range(0, 3):
        best_games.append(games[i])

    popular_games = Game.objects.all().order_by('rates').reverse()
    most_popular = []

    for i in range(0, 3):
        most_popular.append(popular_games[i])

    commented_games = Game.objects.all().order_by('reviews').reverse()
    most_commented = []

    for i in range(0, 3):
        most_commented.append(commented_games[i])

    context = {
        'categories': categories,
        'best_games': best_games,
        'most_popular': most_popular,
        'most_commented': most_commented,
    }

    return render(request, 'rankings.html', context=context)
