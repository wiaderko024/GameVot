from django.urls import path
from .views import home_page, rankings_page, search_page


urlpatterns = [
    path('', home_page, name='home_page'),
    path('search/<str:wanted>/', search_page, name='search_page'),
    path('rankings/', rankings_page, name='rankings_page'),
]
