from rest_framework import serializers
from news.models import *
from django.contrib.auth.models import User


class NewsSerialiser(serializers.ModelSerializer):
    tags_name = serializers.CharField(source='tags.name', read_only=True)
    class Meta:
        model = News
        fields = ('title', "created_time" , "author" , "category","tags",'views_count','tags_name')


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
