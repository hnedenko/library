from django.urls import path
from .views import BooksAPI

urlpatterns = [
    path('', BooksAPI.as_view())
]
