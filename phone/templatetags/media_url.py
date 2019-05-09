import re
from django.utils.safestring import mark_safe
from django.template import Library
from django.utils.translation import get_language_info,get_language
from plan.models import *

register = Library()


@register.filter(name='media_url')
def media_url(value):
   if isinstance(value,PlanPhone):
        print(value.planphoneimages.all().order_by('id')[0].image.url,"image utl")
        return  value.planphoneimages.all().order_by('id')[0].image.url
   return settings.MEDIA_URL+"scrapped/"+value.stores.all()[0].store.lower()+"/"+value.images.all().order_by('id')[0].path


@register.filter(name='brand_filter')
def brand_filter(value):
    return value.brands.all()[0].name


@register.filter(name='media_safe_url')
def media_safe_url(value):
    #  settings.MEDIA_URL + "scrapped/" + phone.stores.all()[0].store.lower() + "/" + phone.images.all()[0].path
    s=settings.MEDIA_URL + "scrapped/" + value.stores.all()[0].store.lower() + "/" + value.images.all().order_by('id')[0].path
    return "-".join(s.split("/"))


@register.filter(name='operator_logo')
def operator_logo(value):
    print("image field value")
    print(type(value))
    # #  settings.MEDIA_URL + "scrapped/" + phone.stores.all()[0].store.lower() + "/" + phone.images.all()[0].path
    # s=settings.MEDIA_URL + "scrapped/" + value.stores.all()[0].store.lower() + "/" + value.images.all().order_by('id')[0].path
    return settings.MEDIA_URL + str(value)


@register.filter(name='split')
def split(value):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '-', value)


@register.filter(name='get_local_name')
def get_local_name(lang):
    return get_language_info(lang)['name_local']


@register.filter(name='plan_count_for_device')
def plan_count_for_device(obj):

    count = 0
    if isinstance(obj,PlanPhone):

        count = DeviceInstallment.objects.filter(phone__in=DeviceRam.objects.filter(device_phone=obj)).count()

        image = settings.MEDIA_URL + obj.planphoneimages.first().image.name
        if count > 0:
            st = '<a href="/mobileplans/operators/?phone_name={name}&phone_slug={slug}&phone_media={image}"' \
                 ' class="available_in_12_plans"> Available in {count} Plans</a>'.\
                format(slug=obj.id, count=count, image=image, name=obj.name)

            return mark_safe(st)
        else:
           return mark_safe("")
    else:

        return mark_safe("")


# def buy_mobile_check(obj):
#     if isinstance(obj,Phone):
#         return True
#     return False
@register.filter(name='custom_name')
def custom_name(name,args):
    var = (" ".join(name.split(" ")[:int(args)])).replace(",", "").replace("-", "").replace("(", "") \
        .replace(")", "").strip()
    return var



