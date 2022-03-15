from atexit import register
from django import template
from main.models import *

register = template.Library()



@register.simple_tag()
def get_categories():
    return Category.objects.all