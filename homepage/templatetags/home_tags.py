from django.utils.translation import get_language_info,get_language

from django import template
register = template.Library()

@register.filter(name='get_local_name')
def get_local_name(lang):
    return get_language_info(lang)['name_local']
