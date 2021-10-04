from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Rate
from games.models import Game
from categories.models import Category


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

                game.rates += 1

                if game.avg_rate is None:
                    game.avg_rate = float(instance.rate)
                else:
                    rates = Rate.objects.filter(game=game)

                    tmp = 0
                    for rate in rates:
                        tmp += rate.rate

                    game.avg_rate = tmp / len(rates)
                    game.save()
        except (KeyError, Rate.rate.DoesNotExist):
            print(KeyError)

        return redirect('games:game_page', game.slug)

    return redirect('users:login')


@login_required
def edit_review(request, id):
    categories = Category.objects.all()

    if request.method == 'POST':
        wanted = request.POST.get('search')
        return redirect('search_page', wanted)

    context = {
        'categories': categories,
    }

    return render(request, 'edit_review.html', context=context)
