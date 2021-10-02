from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category
from games.models import Game


def category_page(request):
    category_name = request.path.split('/')[2]

    categories = Category.objects.all()
    category = Category.objects.get(name=category_name)
    games = Game.objects.filter(category=category)

    if request.method == 'POST':
        wanted = request.POST.get('search')
        return redirect('search_page', wanted)

    context = {
        'categories': categories,
        'category': category,
        'games': games,
    }

    return render(request, 'category.html', context=context)
