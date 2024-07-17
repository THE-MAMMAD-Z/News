from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import News, Category, Tag, Comment, Favorite
from .forms import CommentForm
from django.views import View
from django.contrib import messages

class BaseNewsView(View):
    def get_common_context(self):
        category = Category.objects.annotate(news_count=Count('news'))
        latest = News.objects.order_by('-created_time')[:4]
        tags = Tag.objects.all()[:10]
        return {
            'category': category,
            'latest': latest,
            'tags': tags
        }

class NewsListView(BaseNewsView):
    def get(self, request):
        news = News.objects.all()
        paginator = Paginator(news, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = self.get_common_context()
        context.update({
            'news': news,
            'page_obj': page_obj
        })
        return render(request, "news/blog.html", context)

class NewsDetailView(BaseNewsView):
    def get(self, request, num):
        news = News.objects.get(pk=num)
        news.views_count += 1
        news.save()
        comments = Comment.objects.filter(post=news, Active=True)
        
        context = self.get_common_context()
        context.update({
            'news': news,
            'comments': comments,
            'form': CommentForm()
        })
        return render(request, "news/blog_details.html", context)

    def post(self, request, num):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print("Form is not valid:", form.errors)
            return self.get(request, num)  # Return the same page with errors

class CategoryView(BaseNewsView):
    def get(self, request, name):
        news = News.objects.filter(category__name=name)
        cat_count = Category.objects.count()
        
        context = self.get_common_context()
        context.update({
            'news': news,
            'name': name,
            'cat': cat_count
        })
        return render(request, "news/categori.html", context)

class SearchView(BaseNewsView):
    def get(self, request):
        query = request.GET.get('q', '')
        posts = News.objects.filter(content__icontains=query)
        
        context = self.get_common_context()
        context.update({"page_obj": posts})
        return render(request, 'news/blog.html', context)

@login_required
class FavoriteView(BaseNewsView):
    def get(self, request):
        saved = Favorite.objects.filter(user=request.user)
        paginator = Paginator(saved, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = self.get_common_context()
        context.update({'page_obj': page_obj})
        return render(request, 'news/favorite.html', context)

@login_required
def save_favorite(request, post_id):
    user = request.user
    if not Favorite.objects.filter(user=user, post_id=post_id).exists():
        Favorite.objects.create(user=user, post_id=post_id)
        messages.success(request, 'Post saved as a favorite.')
    else:
        messages.warning(request, "Post is already saved as a favorite.")
    return redirect('news:news')

class TagView(BaseNewsView):
    def get(self, request, tag_name):
        # Fetch news articles related to the specified tag
        blog_tags = News.objects.filter(tags__name=tag_name)
        print(blog_tags)
        # Create the context with common items and specific blog tags
        context = self.get_common_context()
        context.update({
            'page_obg': blog_tags,  # Use 'blog_tags' instead of 'page_obj'
        })
        
        return render(request, 'news/tags.html', context)
