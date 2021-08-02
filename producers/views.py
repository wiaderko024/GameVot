from django.shortcuts import render
from .models import Producer


def all_producers(request):
    producers = Producer.objects.all()

    context = {
        'producers': producers,
    }

    return render(request, 'all_producers.html', context=context)
