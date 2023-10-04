from rest_framework import serializers
from api.models import Article
from django.contrib.auth.models import User


class ArticleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', "author" , "content" , "created","status",'slug')


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'