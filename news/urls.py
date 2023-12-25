
from django.urls import path
from .views import (
    sorted_news_json_view,
    sorted_politics_news_json_view,
    sorted_regions_news_json_view,
    sorted_investments_news_json_view,
    detail_news,
    themes,
    search_word,
    news_of_the_day
    )

urlpatterns = [
    path('/', sorted_news_json_view),
    path("region/", sorted_regions_news_json_view),
    path("politics/",sorted_politics_news_json_view ),
    path("investments/", sorted_investments_news_json_view),
    path("<int:id>/", detail_news),
    path("themes/", themes),
    path("search/<str:word>/", search_word),
    path("day/", news_of_the_day)
]
