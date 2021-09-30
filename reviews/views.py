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

                all_rates = Rate.objects.filter(game=game)
                tmp = 0

                for r in all_rates:
                    tmp += r.rate

                game.avg_rate = tmp / len(all_rates)
                game.save()
            else:
                Rate.objects.create(game=game, user=request.user, rate=rate)
                # logic for counting rates and average rate for CREATE option is in activities.signals file
        except (KeyError, Rate.rate.DoesNotExist):
            print(KeyError)

        return redirect('games:game_page', game.slug)

    return redirect('users:login')
