from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import NewsListCreateSerializer, NewsSerializer
from .models import News

class NewsListCreateAPIView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListCreateSerializer

    @action(detail=True, methods=['POST'])
    def toggle_like(self, request, pk=None):
        news = self.get_object()
        news.likes_count+=1
        data = {'likes_count':news.likes_count}
        return JsonResponse(data,safe = False)

class NewsRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
