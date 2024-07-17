from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('news/',views.NewsListView.as_view(), name='news'),
    path('news-detail/<int:num>/',views.NewsDetailView.as_view() , name='detail'),
    path('category/<str:name>/',views.CategoryView.as_view() , name="category"),
    path('search/',views.SearchView.as_view() , name="search"),
    path('favorite/',views.FavoriteView, name='favorite'),
    path('save_favorite/<int:post_id>/', views.save_favorite, name='save_favorite'),
    path('tags/<str:tag_name>/',views.TagView.as_view() , name='tag')

]
