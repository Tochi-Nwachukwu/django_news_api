from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('headline', 'news_link', 'stories',
                  'image_links', 'news_authors', 'published_date')
