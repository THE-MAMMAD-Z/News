from django.contrib import admin
from . models import News , Category , Comment , Favorite , Tag 

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_time' ]
    search_fields = ['title' , 'content']


class CommentAdmin(admin.ModelAdmin):
    list_dispaly=['name','created_time']
    search_fields=('subject','message')


admin.site.register(News,NewsAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Tag)
