from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from games.models import Game


def category_page(request):
    category_name = request.path.split('/')[2]

    categories = Category.objects.all()
    category = Category.objects.get(name=category_name)
    games = Game.objects.filter(category=category)

    context = {
        'categories': categories,
        'category': category,
        'games': games,
    }

    return render(request, 'category.html', context=context)
