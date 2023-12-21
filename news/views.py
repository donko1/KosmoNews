
from django.http import JsonResponse, HttpResponse
from .models import News  
from KosmoNews import logging
from django.conf import settings

def formatNewForDict(New):
    return {
        "date": New.date,
        "title": New.title,
        "article_text": New.article_text,
        "theme": New.theme
    }

def themes(request):
    themes = settings.THEMES
    return JsonResponse(themes, safe=False)

def helloWorld(request):
    return HttpResponse("Hello world")

def sorted_news_json_view(request):
    all_news = News.objects.all().order_by('-date')  
    news_list = list(all_news.values())  
    logging.log(f'"/" - {all_news[0]}')
    return JsonResponse(news_list, safe=False)

def sorted_politics_news_json_view(request):
    politics_news = News.objects.filter(theme='theme1').order_by('-date')  
    politics_news_list = list(politics_news.values()) 
    logging.log(f'"/politics" - {politics_news_list[0]}')
    return JsonResponse(politics_news_list, safe=False)

def sorted_regions_news_json_view(request):
    regions_news = News.objects.filter(theme='theme2').order_by('-date')  
    regions_news_list = list(regions_news.values())
    logging.log(f'"/region" - {regions_news_list[0]}')  
    return JsonResponse(regions_news_list, safe=False)

def sorted_investments_news_json_view(request):
    investments_news = News.objects.filter(theme='theme3').order_by('-date')  
    investments_news_list = list(investments_news.values())  
    logging.log(f'"/investments" - {investments_news_list[0]}')
    return JsonResponse(investments_news_list, safe=False)

def detail_news(request, id):
    news = News.objects.get(pk=id)
    data = formatNewForDict(news)
    logging.log(f"News Detail - {data}")
    return JsonResponse(data, safe=False)
