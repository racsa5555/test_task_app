from django.urls import path
from .views_api import *

urlpatterns = [
    path('news/', NewsListCreateAPIView.as_view()),
    path('news/<int:pk>/', NewsRetrieveDestroyAPIView.as_view()),
]
