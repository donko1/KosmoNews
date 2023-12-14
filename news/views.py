from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import News  


# Create your views here.

def helloWorld(request):
    return HttpResponse("Hello world")

def sorted_news_json_view(request):
    all_news = News.objects.all().order_by('-date')  
    news_list = list(all_news.values())  
    return JsonResponse(news_list, safe=False)
