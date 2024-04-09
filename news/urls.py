# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', news_list, name='news_list'),
    path('load_more/', load_more_news, name='load_more_news'),
]
