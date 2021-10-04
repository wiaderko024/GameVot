from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Rate, Review
from games.models import Game
from categories.models import Category
from .forms import ReviewForm


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
def edit_review(request, review_id):
    categories = Category.objects.all()

    review = Review.objects.get(pk=review_id)
    form = ReviewForm(instance=review)

    if request.method == 'POST':
        if request.POST.get('search') is not None:
            return redirect('search_page', request.POST.get('search'))

        form = ReviewForm(request.POST or None, request.FILES or None, instance=review)
        if form.is_valid():
            form.save()
            return redirect('games:game_page', review.game.slug)

    context = {
        'categories': categories,
        'form': form,
    }

    return render(request, 'edit_review.html', context=context)
