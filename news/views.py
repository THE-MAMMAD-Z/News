from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from django.core.paginator import Paginator
from .models import News , Category , Comment , Favorite , Tag
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def news(request):
    news = News.objects.all()
    paginator = Paginator(news, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    art = News.objects.filter(category__name="ART").count()
    s = News.objects.filter(category__name="SPORT").count()
    tr = News.objects.filter(category__name="TRAVEL").count()
    tec = News.objects.filter(category__name="TECHNOLOGI").count()
    f = News.objects.filter(category__name="FOOD").count()
    c = News.objects.filter(category__name="CAR").count()
    latest = News.objects.order_by('-created_time')[:4]
    
    tags = Tag.objects.all()[:10]

    context={
        "news":news,
        'page_obj': page_obj,
        "art":art,"s":s,"tr":tr,"tec":tec,"f":f,"c":c,
        "latest":latest,
        "tags": tags
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
    news.views_count += 1
    news.save()
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
    


@login_required
def favorite(request):
    saved = Favorite.objects.filter(user=request.user)
    paginator = Paginator(saved, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    art = News.objects.filter(category__name="ART").count()
    s = News.objects.filter(category__name="SPORT").count()
    tr = News.objects.filter(category__name="TRAVEL").count()
    tec = News.objects.filter(category__name="TECHNOLOGI").count()
    f = News.objects.filter(category__name="FOOD").count()
    c = News.objects.filter(category__name="CAR").count()
    latest = News.objects.order_by('-created_time')[:4]
    
    tags = Tag.objects.all()[:10]
    return render(request, 'news/favorite.html', {"page_obj": page_obj})


def save_favorite(request, post_id):
    user = request.user  # Get the logged-in user
    
    # Check if the user has already saved this post as a favorite
    if not Favorite.objects.filter(user=user, post_id=post_id).exists():
        favorite = Favorite(user=user, post_id=post_id)
        favorite.save()
        messages.success(request, 'Post saved as a favorite.')
        return redirect('news:news')
    else:
        messages.warning(request,"Post is already saved as a favorite.")
        return redirect('news:news')
    


def tag(request,tag_name):
    blog_tags=News.objects.filter(tags__name=tag_name)
    
    art = News.objects.filter(category__name="ART").count()
    s = News.objects.filter(category__name="SPORT").count()
    tr = News.objects.filter(category__name="TRAVEL").count()
    tec = News.objects.filter(category__name="TECHNOLOGI").count()
    f = News.objects.filter(category__name="FOOD").count()
    c = News.objects.filter(category__name="CAR").count()
    latest = News.objects.order_by('-created_time')[:4]
    
    tags = Tag.objects.all()[:10]
    context = {
        "art":art,"s":s,"tr":tr,"tec":tec,"f":f,"c":c,
        "latest":latest,
        "tags": tags,
        "page_obg":blog_tags
    }
    return render(request,'news/tags.html',context)