from django.urls import path
from .views import AuthorsAPI

urlpatterns = [
    path('', AuthorsAPI.as_view())
]
