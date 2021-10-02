from django.shortcuts import render, redirect
from .models import Producer
from categories.models import Category
from games.models import Game


def all_producers(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        wanted = request.POST.get('search')
        return redirect('search_page', wanted)

    producers = Producer.objects.all()

    context = {
        'producers': producers,
        'categories': categories,
    }

    return render(request, 'all_producers.html', context=context)


def producer_page(request, producer_slug):
    categories = Category.objects.all()

    if request.method == 'POST':
        wanted = request.POST.get('search')
        return redirect('search_page', wanted)

    producer = Producer.objects.get(slug=producer_slug)
    games = Game.objects.filter(producer=producer)

    context = {
        'producer': producer,
        'categories': categories,
        'games': games,
    }

    return render(request, 'producer.html', context=context)
