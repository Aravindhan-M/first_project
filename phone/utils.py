import re
import random
import string
from itertools import groupby
from django.conf import settings


from django.utils.text import slugify

pattern = re.compile(r'[0-9]+')

def get_available_currency():
    CURRENCY = (
        ('DZD', 'Algerian dinar'),
        ('BHD', 'Bahraini dinar'),
        ('EGP', 'Egyptian pound'),
        ('IQD', 'Iraqi dinar'),
        ('JOD', 'Jordanian dinar'),
        ('KWD', 'Kuwaiti dinar'),
        ('LBP', 'Lebanese Pound'),
        ('LYD', 'Libyan dinar'),
        ('MAD', 'Moroccan dirham'),
        ('OMR', 'Omani rial'),
        ('ent', 'Palestine pound'),
        ('QAR', 'Qatari riyal'),
        ('SAR', 'Saudi riyal'),
        ('SSP', 'Sudanese pound'),
        ('SYP', 'Syrian pound'),
        ('TND', 'Tunisian dinar'),
        ('AED', 'United Arab Emirates dirham'),
        ('YER', 'Yemeni rial'),
        ('USD', 'United States Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'GBP'),


    )
    return CURRENCY

def get_available_languages():
    return settings.LANGUAGES


def get_planphone_count(phone):
    pass
#     print("m2m count")
#     print(Plan.objects.filter(phone=phone).count())
#     return Plan.objects.filter(phone=phone).count()
#

def get_planphoneimage_path(phone):
    # settings.MEDIA_URL+"/scrapped/"+value.images.all()[0].path
    return settings.MEDIA_URL +phone.planphoneimages.all()[0].image.name


def get_image_path(phone):
    # if isinstance(phone,PlanPhone):
    #     return  phone.planphoneimages.all().order_by('id')[0].image.url
    return settings.MEDIA_URL+"scrapped/"+phone.stores.all()[0].store.lower()+"/"+phone.images.all().order_by('id')[0].path



def refine_internal(lists):
    li = [a.replace(" ", "") for a in lists if a is not None and "GB" in a and a.count("GB") == 1]
    return list(set(li))



def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def get_number(s):
    return pattern.findall(s)


def group_phone(plan_phone,phone):
    plan = list(plan_phone)
    phone = list(phone)
    print(phone,"phoneeee")
    phone_id = []
    buy_mobile = []
    plan_phone_id = []
    check = []
    for d in plan:
        li = list(d.values())
        check.append(li[1].lower() if li[1] else li[1])
        plan_phone_id.append(li[0])
    for key, group in groupby(phone, lambda x: x['title_tst'].lower()):

        for thing in group:
            if key not in check:
                phone_id.append(thing['id'])
            else:
                buy_mobile.append(thing['title_tst'].lower())
    return phone_id, plan_phone_id, buy_mobile
