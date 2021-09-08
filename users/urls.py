from django.urls import path
from .views import sign_up_page, login_page


app_name = 'users'

urlpatterns = [
    path('login/', login_page, name='login'),
    path('sign-up/', sign_up_page, name='sign_up'),
]
