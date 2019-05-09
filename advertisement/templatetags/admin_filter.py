from django import template

register = template.Library()


@register.filter(name='caps')
def caps(value):
    if value == 'adsl':
        value = "fixed internet"
    if value == 'mobileplans':
        value = "Mobile Plans"
    if value == 'phones':
        value = "Mobile Phones"
    if value == 'plan':
        value = "Mobile Internet"
    if value == 'register':
        value = "REGISTER"
    if value == 'operators':
        value = "OPERATORS"

    return value.upper()


@register.filter(name='zone_filter')
def zone_filter(value, row):
    zones = []
    for val in value:
        zones.append(val.filter(page=row))
    return zones


@register.simple_tag(name='data_filter')
def data_filter(value, page, zone):
    data = []
    for val in value:
        if val.zone == zone and val.page == page:
            data.append(val)
    return data



