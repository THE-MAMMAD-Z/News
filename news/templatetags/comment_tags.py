from django import template
from news.models import Comment

register = template.Library()

@register.simple_tag
def get_comment_count(post_id):
    return Comment.objects.filter(post_id=post_id).count()