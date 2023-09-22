from django import template
from news.models import Category
register = template.Library()

@register.inclusion_tag('base/category.html')
def tedad():
    cat = 15
    return {"cat":cat}

