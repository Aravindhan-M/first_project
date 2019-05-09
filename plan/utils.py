import random
import string
from django.conf import settings
from django.utils.text import slugify
from django.db.models import Max
from django.apps import apps


def get_opt_help_text():
    CONTENT_HELP_TEXT = ' '.join(['<p>OTP1 = <b>Package One Time Setup Fees</b><br/>',
                                  'OTP2 = <b>Package One Time Setup Fees + Device Upfront One Time Payment</b><br/>',
                                  'OTP3= <b>Package One Time Setup Fees +  2 x(Package Fees) +2 x '
                                  '(Device Installment Value)</b>',
                                  '<br/>'])

    return CONTENT_HELP_TEXT


def get_mf_help_text():
    CONTENT_HELP_TEXT = ' '.join(['<p>MF1 = <b>Package Fees</b><br/>',
                                  'MF2 = <b>Package Fees + Device Installment Value</b><br/>',

                                  '<br/>'])

    return CONTENT_HELP_TEXT


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_one_time_payment_method():
    method = (
        ('OTP1', 'OTP1'),
        ('OTP2', 'OTP2'),
        ('OTP3', 'OTP3'),

    )
    return method


def monthly_fee_calculation_method():
    method = (
        ('MF1', 'MF1'),
        ('MF2', 'MF2'),

    )
    return method


def get_available_apps():

    APPS = (
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('Snapchat', 'Snapchat'),
        ('Viber', 'Viber'),
        ('WhatsApp', 'WhatsApp'),
        ('Skype', 'Skype'),
        ('Tango', 'Tango'),
        ('YouTube', 'YouTube'),
        ('imo', 'imo'),
        ('LinkedIn', 'LinkedIn'),
    )
    return APPS


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


def get_plan_phone_image_path(phone):
    # settings.MEDIA_URL+"/scrapped/"+value.images.all()[0].path
    return settings.MEDIA_URL +phone.planphoneimages.all()[0].image.name


def donut_calculation(context):

    qs = context['plans']

    if qs.model.__name__ == 'FixedInternet':
        context['maxi'] = qs.aggregate(Max('upload_speed'))
    else:

        context['max_message_donut'] = qs.aggregate(Max('message__donut_message_val'))
        context['max_data_donut'] = qs.aggregate(Max('data__donut_data_val'))
        context['max_call_donut'] = qs.aggregate(Max('call__donut_call_val'))
    return context


def donut_calculation_plan_detail(qs,context):
    context['max_message_donut'] = qs.aggregate(Max('message__donut_message_val'))
    context['max_data_donut'] = qs.aggregate(Max('data__donut_data_val'))
    context['max_call_donut'] = qs.aggregate(Max('call__donut_call_val'))

    return context


def get_device_image_path(device):

   return  settings.MEDIA_URL+ device.deviceimage.image.name


def get_available_data(self):

    exclude = "donut_{donut}_val".format(donut=self.__class__.__name__.lower())

    return {field.verbose_name: user_friendly_value(field.value_from_object(self)) for field in self._meta.local_fields if
            field.value_from_object(self) and field.name not in ['id', 'plan',exclude]}


def user_friendly_value(val):
    if isinstance(val, list):
        return ",".join(val)
    if isinstance(val, bool):
        return "Yes"
    return val


# def get_exchange(func):
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper


def calculate_otp(plan,sim=None):
    try:
        install = plan.device_installment_plan.first()
    except IndexError:
        install = None
    value = 0

    if install:
        if sim:
            if plan.otp_method == 'OTP1':
                value = plan.one_time_setup_fee
            if plan.otp_method == 'OTP2':
                plan_phone_upfront = install.device_upfront_otp
                value = plan.one_time_setup_fee + plan_phone_upfront
            if plan.otp_method == 'OTP3':
                value = plan.one_time_setup_fee + (2 * plan.fee) + (2 * install.installment_value)
        else:
            if install.otp_method == 'OTP1':
                value = plan.one_time_setup_fee
            if install.otp_method == 'OTP2':
                plan_phone_upfront = install.device_upfront_otp
                value = plan.one_time_setup_fee + plan_phone_upfront
            if install.otp_method == 'OTP3':
                value = plan.one_time_setup_fee + (2 * plan.fee) + (2 * install.installment_value)

    return int(value)


def calculate_mf(plan,sim=None):
    try:
        install = plan.device_installment_plan.first()
    except IndexError:
        install = None

    value = 0
    if sim:
        if plan.mf_method == 'MF1':
            value = plan.fee
        if plan.mf_method == 'MF2':
            if install:
                value = plan.fee + install.installment_value
            else:
                value = plan.fee
    else:
        if install:

            if install.mf_method == 'MF1':
                value = plan.fee
            if install.mf_method == 'MF2':
                if install:
                    value = plan.fee + install.installment_value
                else:
                    value = plan.fee
        else:
            value = plan.fee

    return int(value)




