from django.shortcuts import render


def all_producers(request):
    return render(request, 'all_producers.html')
