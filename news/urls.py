from django.urls import path
from .views import *

urlpatterns = [
    path('', news_list, name='news_list'),
    path('load_more/', load_more_news, name='load_more_news'),
    path('get_likes/<int:id>/', get_likes_count, name='get_likes_count'),
    path('get_dislikes/<int:id>/', get_dislikes_count, name='get_dislikes_count'),
    path('<int:id>/',retrieve_news,name = 'retrieve_news'),
    path('find_news/',find_news,name = 'find_news'),
    path('find_news_by_tag/',find_news_by_tag,name = 'find_news_by_tag')
]
