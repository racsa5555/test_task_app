from typing import Iterable
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    
    def __str__(self):
        return f'{self.name}'

class News(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    image = models.ImageField(upload_to='media')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add = True)
    likes_count = models.PositiveIntegerField(default = 0)
    dislikes_count = models.PositiveIntegerField(default = 0)
    views = models.PositiveIntegerField(default = 0)
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
    def __str__(self):
        return f'{self.title} -> {self.id}'

