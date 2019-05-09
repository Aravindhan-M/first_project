import math

from django import template
from fixed_internet.models import FixedInternet
from django.conf import settings

register = template.Library()
fixed_plan = FixedInternet.active_fixed_internet.all()


@register.simple_tag(name='get_fixed_count',takes_context=True)
def get_fixed_count(context):
    req = context['request']
    country = req.session.get('country', "SA")
    return fixed_plan.filter(country__country_code=country).count()