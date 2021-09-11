from django.shortcuts import render, redirect
from .models import Game
from categories.models import Category
from reviews.models import Review, Rate
from reviews.forms import ReviewForm
from activities.models import Activity


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
    reviews = Review.objects.filter(game=game)
    rate_scale = [i for i in range(1, 11)]
    form = ReviewForm()

    if request.user.is_authenticated:
        user_rate = Rate.objects.filter(user=request.user, game=game)
        Activity.objects.create(visit=True, game_id=game.id, user=request.user)
    else:
        user_rate = None
        Activity.objects.create(visit=True, game_id=game.id, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            Review.objects.create(user=request.user, game=game, text=text)
            return redirect('games:game_page', game.slug)

    context = {
        'game': game,
        'categories': categories,
        'reviews': reviews,
        'form': form,
        'rate_scale': rate_scale,
        'user_rate': user_rate,
    }

    return render(request, 'game.html', context=context)
