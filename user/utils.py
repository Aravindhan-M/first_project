import urllib
import json
from django.conf import settings
from django.utils.translation import gettext_lazy
from plan.models import operators
operator = operators.objects.values('operator')
GOOGLE_CAPTCHA_URL = 'https://www.google.com/recaptcha/api/siteverify'


def get_mobile_operators():
    for op in (list(operator)):
        value = gettext_lazy(op['operator'])
        yield (value,value)


def re_captcha_validation(re_captcha_response):
    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': re_captcha_response
    }
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(GOOGLE_CAPTCHA_URL, data)
    response = urllib.request.urlopen(req)
    result = json.load(response)
    if result['success']:
        return True
    else:
        return False
