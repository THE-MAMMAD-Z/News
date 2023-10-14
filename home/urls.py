from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name='home'
urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',cache_page(60 * 15)(views.about),name='about'),
]
