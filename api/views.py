# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView ,  DestroyAPIView, ListAPIView , ListCreateAPIView , RetrieveAPIView
from django.views.generic import ListView
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .serializers import NewsSerialiser , UserSerialiser
from django.contrib.auth.models import User
from news.models import News


# class NewsListtest(ListView):
#     def get_queryset(self):
#         return News.objects.filter(status=True)
    

class NewsList(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class =NewsSerialiser
    #authentication_classes = (SessionAuthentication,)


class NewsDetail(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class =NewsSerialiser


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
