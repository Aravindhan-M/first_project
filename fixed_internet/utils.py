import random
import string
from django.db.models import Max
from django.utils.text import slugify
from django.db.models.fields.related import RelatedField

def donut_calculation(context):
    qs = context['plans']

    context['maxi'] = qs.aggregate(Max('upload_speed'))
    return context


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


def user_friendly_value(field,self):
    currency = ['monthly_fee','upfront_payment_per_year', 'upfront_payment_half_yearly', 'upfront_payment_quarterly']
    data = ['download_speed', 'upload_speed', 'data_quota']
    val = field.value_from_object(self)

    if field.name in currency:
        return str(val) + ":currency"
    if field.name in data:
        return str(val) + ":data"
    if isinstance(field,RelatedField):
        return field.value_from_object(self)
    if isinstance(val, list):
        return ",".join(val)
    if isinstance(val, bool):
        return "Yes"
    return val


def get_available_data(self):

    table_data = ['name', 'pay_type', 'description', 'short_description', 'monthly_fee',
                  'fee_notes', 'upfront_payment_per_year', 'upfront_payment_half_yearly', 'upfront_payment_quarterly',
                  'download_speed', 'upload_speed', 'data_quota', 'benefits', 'available_for']

    dict = {field.verbose_name: user_friendly_value(field, self) for field in self._meta.local_fields if
            field.value_from_object(self) and field.name in table_data}

    # print(dict)
    return dict
