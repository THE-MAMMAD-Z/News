from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from django.core.paginator import Paginator
from .models import News , Category , Comment , Favorite , Tag
from .forms import CommentForm 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count


def news(request):
    news = News.objects.all()
    paginator = Paginator(news, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    category = Category.objects.annotate(news_count=Count('news'))
    
    latest = News.objects.order_by('-created_time')[:4]
    
    tags = Tag.objects.all()[:10]

    context={
        "news":news,
        'page_obj': page_obj,
        'category' : category,
        "latest":latest,
        "tags": tags
    }
    return render(request,"news/blog.html",context)

def detail_news(request,num):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form is valid and saved!")
            return redirect('/')
        else:
            print("Form is not valid:", form.errors)
    form=CommentForm()
    news = News.objects.get(pk=num)
    news.views_count += 1
    news.save()
    category = Category.objects.annotate(news_count=Count('news'))
    comments=Comment.objects.filter(post=news,Active=1)
    latest = News.objects.order_by('-created_time')[:4]
    tags = Tag.objects.all()[:10]
    context = {
        "news":news ,
        "comments" : comments ,
        "form" : form,
        "latest":latest,
        "tags": tags,
        'category' : category,
    }
    return render(request , "news/blog_details.html",context)


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
    paginator = Paginator(saved, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    category = Category.objects.annotate(news_count=Count('news'))

    latest = News.objects.order_by('-created_time')[:4]
    
    tags = Tag.objects.all()[:10]
    return render(request, 'news/favorite.html', context = {
        'category' : category,
        "latest":latest,
        "tags": tags,
        'page_obj': page_obj,
    })


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
    category = Category.objects.annotate(news_count=Count('news'))
    latest = News.objects.order_by('-created_time')[:4]
    tags = Tag.objects.all()[:10]
    context = {
        'category' : category,
        "latest":latest,
        "tags": tags,
        "page_obg":blog_tags
    }
    return render(request,'news/tags.html',context)