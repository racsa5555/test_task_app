from django.shortcuts import render
from django.http import JsonResponse
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
    news = News.objects.get(id = id)
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
    return render(request, 'news/retrieve_news.html', {'news': news})
