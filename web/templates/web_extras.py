from django import template
from web.models import Category

register = template.Library()

@register.inclusion_tag('web/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}