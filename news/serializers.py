from rest_framework import serializers

from .models import News

class NewsListCreateSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    views = serializers.ReadOnlyField()
    
    def get_tags(self,obj):
        data = []
        for x in obj.tags.all():
            data.append(x.name)
        return data

    class Meta:
        model = News
        exclude = ['likes_count','dislikes_count']

class NewsSerializer(NewsListCreateSerializer):
    
    class Meta:
        fields = '__all__'
        model = News