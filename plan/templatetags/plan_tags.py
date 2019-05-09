import math

from django import template
from plan.models import Plan,operators
from django.conf import settings
from utils.util import get_exchange_rate
from fixed_internet.models import FixedInternet
register = template.Library()
plan = Plan.mobile_plan_objects.all()
internet = Plan.mobile_internet_objects.all()


def round_up(n,decimals=1):
    multiplier = 10 ** decimals

    return math.ceil(n * multiplier) / multiplier


@register.simple_tag(name='get_plan_count',takes_context=True)
def get_plan_count(context):
    req = context['request']
    country = req.session.get('country',"SA")

    return plan.filter(country__country_code=country).count()


@register.simple_tag(name='get_mobile_plan_count',takes_context=True)
def get_mobile_plan_count(context):
    req = context['request']
    country = req.session.get('country',"SA")

    return internet.filter(country__country_code=country).count()


@register.simple_tag(name='get_prepaid_count')
def get_prepaid_count():
    return plan.filter(pay_type='prepaid').count()


@register.simple_tag(name='get_postpaid_count')
def get_postpaid_count():
    return plan.filter(pay_type='postpaid').count()


@register.filter(name='data_converter')
def data_converter(value):
    if value < 999:
        return "{data} MB".format(data=value)

    return "{data} GB".format(data=round_up(value/1000))


@register.inclusion_tag('plan/operator_details.html', takes_context=True)
def operator(context,type):
    req = context['request']
    country = req.session.get('country', "SA")
    if type == "plan":
        op = plan.values('operator_id__operator').filter(operator_id__country__country_code=country)\
            .distinct()
    if type == "internet":
        op = internet.values('operator_id__operator').filter(operator_id__country__country_code=country)\
            .distinct()
    if type == "fixed":
        op = FixedInternet.active_fixed_internet.values('operator_id__operator').filter(operator_id__country__country_code=country)\
            .distinct()
    return {
       "context" : op
    }


@register.inclusion_tag('plan/operator_images.html', takes_context=True)
def operator_images(context,type):
    req = context['request']

    country = req.session.get('country', "SA")
    if type == "plan":
        op = plan.values('operator_id__image').filter(operator_id__country__country_code=country) \
            .distinct()
    if type == "internet":
        op = internet.values('operator_id__image').filter(operator_id__country__country_code=country) \
            .distinct()
    if type == "fixed":
        op = FixedInternet.active_fixed_internet.values('operator_id__image').filter(
            operator_id__country__country_code=country) \
            .distinct()

    return {
       "context" : op,
        "media" : settings.MEDIA_URL
    }


@register.filter()
def percentof(amount, total):

    if amount is None:
        amount =0
    if total is None:
        total = 0
    try:

        return round((int(amount)/int(total)) * 100)
    except ZeroDivisionError:
        return 0
    except:
        return 0


@register.filter()
def display(val):
    display={

        "fee" : "Lowest Price",
        "-fee": "Highest Price",
        "-message__donut_message_val": "Maximum Message",
        "-data__donut_data_val": "Maximum Data",
        "-call__donut_call_val": "Maximum Minutes"
    }
    try:

        if not val:
            return "Sort By"
        return display[val]
    except Exception:
        return 0


@register.filter()
def firstImage(image):
    try:
        print("first imahge")
        print(type(image))
        print(image.planphoneimages.all()[0].image)

    except ZeroDivisionError:
        return 0

@register.simple_tag(name='exchange_rate',takes_context=True)
def exchange_rate(context,amount):

    if not amount:
        return 0
    rate = 1

    try:

        rate = context['request'].session['currency_rate']
        return int(amount * float(rate))
    except:
        pass
    return amount * rate

from django.utils.encoding import iri_to_uri

from el_pagination import utils

@register.inclusion_tag('el_pagination/show_more.html', takes_context=True)
def show_more1(context, label=None, loading=settings.LOADING, class_name=None):
    """Show the link to get the next page in a Twitter-like pagination.

    Usage::

        {% show_more %}

    Alternatively you can override the label passed to the default template::

        {% show_more "even more" %}

    You can override the loading text too::

        {% show_more "even more" "working" %}

    You could pass in the extra CSS style class name as a third argument

       {% show_more "even more" "working" "class_name" %}

    Must be called after ``{% paginate objects %}``.
    """
    # This template tag could raise a PaginationError: you have to call
    # *paginate* or *lazy_paginate* before including the showmore template.
    data = utils.get_data_from_context(context)
    page = data['page']
    # show the template only if there is a next page
    if page.has_next():
        request = context['request']
        page_number = page.next_page_number()
        # Generate the querystring.
        querystring_key = data['querystring_key']
        querystring = utils.get_querystring_for_page(
            request, page_number, querystring_key,
            default_number=data['default_number'])
        return {
            'label': label,
            'loading': loading,
            'class_name': class_name,
            'path': iri_to_uri(data['override_path'] or request.path),
            'querystring': querystring,
            'querystring_key': querystring_key,
            'request': request,
        }
    # No next page, nothing to see.
    return {}


