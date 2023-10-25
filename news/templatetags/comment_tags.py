from django import template
from news.models import Comment , News

register = template.Library()

@register.simple_tag
def get_comment_count(post_id):
    return Comment.objects.filter(post_id=post_id).count()


@register.simple_tag
def get_view_count():
    popular_posts = News.objects.all().order_by('-views_count')[:5]