from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Rate
from games.models import Game


@login_required
def rate_game(request, game_id, rate):
    if request.user.is_authenticated:
        game = Game.objects.get(pk=game_id)

        try:
            rates = Rate.objects.filter(game=game, user=request.user)
            if rates.exists():
                rates.update(rate=rate)
            else:
                Rate.objects.create(game=game, user=request.user, rate=rate)
        except (KeyError, Rate.rate.DoesNotExist):
            pass

        return redirect('games:game_page', game.slug)

    return redirect('users:login')
