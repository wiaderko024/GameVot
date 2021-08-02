from django.shortcuts import render
from .models import Producer


def all_producers(request):
    producers = Producer.objects.all()

    context = {
        'producers': producers,
    }

    return render(request, 'all_producers.html', context=context)


def producer_page(request, producer_slug):
    producer = Producer.objects.get(slug=producer_slug)

    context = {
        'producer': producer,
    }

    return render(request, 'producer.html', context=context)
