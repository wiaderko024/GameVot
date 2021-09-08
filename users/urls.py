from django.urls import path
from .views import sign_up_page


app_name = 'users'

urlpatterns = [
    path('sign-up/', sign_up_page, name='sign_up'),
]
