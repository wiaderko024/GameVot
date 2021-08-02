from django.shortcuts import render
from .models import Producer
from categories.models import Category


def all_producers(request):
    producers = Producer.objects.all()
    categories = Category.objects.all()

    context = {
        'producers': producers,
        'categories': categories,
    }

    return render(request, 'all_producers.html', context=context)


def producer_page(request, producer_slug):
    producer = Producer.objects.get(slug=producer_slug)
    categories = Category.objects.all()

    context = {
        'producer': producer,
        'categories': categories,
    }

    return render(request, 'producer.html', context=context)
