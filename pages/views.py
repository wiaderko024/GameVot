from django.shortcuts import render, redirect
from categories.models import Category
from games.models import Game
from producers.models import Producer


def home_page(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        wanted = request.POST.get('search')
        return redirect('search_page', wanted)

    games = Game.objects.all().order_by('avg_rate').reverse()
    best_games = []

    for i in range(0, 3):
        best_games.append(games[i])

    games = Game.objects.all().order_by('year').reverse()
    new_games = []

    for i in range(0, 3):
        new_games.append(games[i])

    games = Game.objects.all().order_by('created_at').reverse()
    last_games = []

    for i in range(0, 3):
        last_games.add(games[i])

    context = {
        'categories': categories,
        'best_games': best_games,
        'new_games': new_games,
        'last_games': last_games,
    }

    return render(request, 'index.html', context=context)


def rankings_page(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        wanted = request.POST.get('search')
        return redirect('search_page', wanted)

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


def search_page(request, wanted):
    categories = Category.objects.all()

    if request.method == 'POST':
        wanted = request.POST.get('search')
        return redirect('search_page', wanted)

    games = Game.objects.all()
    producers = Producer.objects.all()
    tmp = wanted.lower()
    games_results = []
    producers_results = []

    for game in games:
        title = game.title.lower()
        if tmp in title:
            games_results.append(game)

    for producer in producers:
        name = producer.name.lower()
        if tmp in name:
            producers_results.append(producer)

    context = {
        'categories': categories,
        'games_results': games_results,
        'producers_results': producers_results,
    }

    return render(request, 'search_page.html', context=context)
