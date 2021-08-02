from django.urls import path
from .views import all_producers


app_name = 'producers'

urlpatterns = [
    path('all-producers', all_producers, name='all_producers_page'),
]
