from django.shortcuts import render
from categories.models import Category


def home_page(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'index.html', context=context)


def rankings_page(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'rankings.html', context=context)
