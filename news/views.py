from django.shortcuts import render
from django.http import JsonResponse
from urllib.parse import unquote

from .models import News

def news_list(request):
    news = News.objects.all()
    per_page = 3
    paginated_news = news[:per_page]

    return render(request, 'news/news.html', {'news': paginated_news})

def load_more_news(request):
    page = int(request.GET.get('page'))
    per_page = int(request.GET.get('perPage'))

    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    news = News.objects.all()[start_index:end_index]
    news_data = []
    for item in news:
        tags_data = [{'name': tag.name, 'id': tag.id} for tag in item.tags.all()]
        news_item_data = {
            'id':item.id,
            'title': item.title,
            'text': item.text,
            'image_url': str(item.image),
            'tags': tags_data,
        }
        news_data.append(news_item_data)
    return JsonResponse(news_data, safe=False)

def get_likes_count(request,id):
    news = News.objects.get(id = id)
    news.likes_count += 1
    news.save()
    data = {'likesCount': news.likes_count}
    return JsonResponse(data)


def get_dislikes_count(request,id):
    news = News.objects.get(id = id)
    news.dislikes_count += 1
    news.save()
    news = News.objects.get(id = id)
    data = {'dislikesCount': news.dislikes_count}
    return JsonResponse(data)


def retrieve_news(request,id):
    news = News.objects.get(id=id)
    news.views += 1
    news.save()
    return render(request, 'news/retrieve_news.html', {'news': news})

def find_news(request):
    query = request.GET.get('query',None)
    
    if query is None:
        return render(request,'news/find_news.html')
    decoded_query = unquote(query)
    news_list = News.objects.filter(tags__name__icontains=decoded_query)
    news_list2 = []
    for news in news_list:
        tags_data = [{'name': tag.name, 'id': tag.id} for tag in news.tags.all()]
        news_item_data = {
            'id':news.id,
            'title': news.title,
            'text': news.text,
            'image_url': str(news.image),
            'tags': tags_data,
        }
        news_list2.append(news_item_data)
    return render(request,'news/find_news.html',{'news_list':news_list2})

def find_news_by_tag(request):
    tag = request.GET.get('tag', None)
    news = News.objects.filter(tags__name__icontains=tag)
    news_data = []
    for item in news:
        tags_data = [{'name': tag.name, 'id': tag.id} for tag in item.tags.all()]
        news_item_data = {
            'id':item.id,
            'title': item.title,
            'text': item.text,
            'image_url': str(item.image),
            'tags': tags_data,
        }
        news_data.append(news_item_data)
    return JsonResponse(news_data, safe=False)