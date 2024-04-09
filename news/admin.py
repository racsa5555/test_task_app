from django.contrib import admin

from .models import News
from .models import Tag

admin.site.register(News)
admin.site.register(Tag)