from django.urls import path
from categories.models import Category
from .views import category_page


app_name = 'categories'

urlpatterns = []

try:
    categories = Category.objects.all()
    for category in categories:
        urlpatterns.append(path(str(category.name + '/'), category_page))
except ImportError as e:
    print(e)
