
from django.urls import path
from .views import helloWorld, sorted_news_json_view

urlpatterns = [
    path('', helloWorld),
    path("newest/", sorted_news_json_view)
]
