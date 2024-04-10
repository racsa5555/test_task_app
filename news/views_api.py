from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import NewsListCreateSerializer, NewsSerializer
from .models import News

class NewsListCreateAPIView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListCreateSerializer

class NewsRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
