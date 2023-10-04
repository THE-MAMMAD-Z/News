# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView ,  DestroyAPIView, ListAPIView , ListCreateAPIView , RetrieveAPIView
from django.views.generic import ListView
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from . models import Article
from .serializers import ArticleSerialiser , UserSerialiser
from django.contrib.auth.models import User

class ArticleListtest(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)
    

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class =ArticleSerialiser
    #authentication_classes = (SessionAuthentication,)


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class =ArticleSerialiser


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class =UserSerialiser
    permission_classes = (IsAdminUser,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class =UserSerialiser
    permission_classes = (IsAdminUser,)


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)

#     def delete(self,request):
#         request.auth.delete()
#         return Response(status=204)
