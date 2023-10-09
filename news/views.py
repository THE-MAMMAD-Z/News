from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import News , Category , Comment
from .forms import CommentForm

def news(request):
    news = News.objects.all()
    paginator = Paginator(news, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    art = News.objects.filter(category__name="ART").count()
    s = News.objects.filter(category__name="SPORT").count()
    tr = News.objects.filter(category__name="TRAVEL").count()
    tec = News.objects.filter(category__name="TECHNOLOGY").count()
    f = News.objects.filter(category__name="FOOD").count()
    c = News.objects.filter(category__name="CAR").count()
    latest = News.objects.order_by('-created_time')[:4]
    context={
        "news":news,
        'page_obj': page_obj,
        "art":art,"s":s,"tr":tr,"tec":tec,"f":f,"c":c,
        "latest":latest
    }
    return render(request,"news/blog.html",context)

def detail_news(request,num):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=CommentForm()
    news = News.objects.get(pk=num)
    comments=Comment.objects.filter(post=news,Active=1)
    return render(request , "news/blog_details.html",{"news":news , "comments" : comments , "form" : form})


def categori(request,name):
    news = News.objects.filter(category__name = name)
    cat = Category.objects.all().count()
    context ={
        "news":news ,
        "name":name ,
        "cat":cat
    }
    return render(request,"news/categori.html", context)


def search(request):
    if request.method == "GET":
        s = request.GET.get('q')
        posts = News.objects.filter(content__contains=s)
        return render(request, 'news/blog.html', {"page_obj": posts})
    



