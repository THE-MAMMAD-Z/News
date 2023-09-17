from django.contrib import admin
from . models import News , Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_time' , 'category']
    search_fields = ['title' , 'content']

admin.site.register(News,NewsAdmin)
admin.site.register(Category)
