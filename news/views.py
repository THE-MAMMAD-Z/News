from django.shortcuts import render
from django.http import HttpResponse

def news(request):
    return render(request,"news/blog.html")

def detail_news(request):
    return render(request , "news/blog_details.html")