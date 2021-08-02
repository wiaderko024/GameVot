from django.urls import path
from .views import all_producers, producer_page


app_name = 'producers'

urlpatterns = [
    path('all-producers/', all_producers, name='all_producers_page'),
    path('<slug:producer_slug>/', producer_page, name='producer_page'),
]
