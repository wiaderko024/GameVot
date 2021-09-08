from django.urls import path
from .views import sign_up_page, login_page, logout_page


app_name = 'users'

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('sign-up/', sign_up_page, name='sign_up'),
]
