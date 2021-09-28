from django.urls import path
from .views import home_page, rankings_page


urlpatterns = [
    path('', home_page, name='home_page'),
    path('rankings/', rankings_page, name='rankings_page'),
]
