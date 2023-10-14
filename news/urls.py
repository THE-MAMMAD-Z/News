from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('news/',views.news, name='news'),
    path('news-detail/<int:num>/',views.detail_news , name='detail'),
    path('category/<str:name>/',views.categori , name="category"),
    path('search/',views.search , name="search"),
    path('favorite/',views.favorite , name='favorite'),
    path('save_favorite/<int:post_id>/', views.save_favorite, name='save_favorite'),


]
