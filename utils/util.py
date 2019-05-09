import urllib.request
import json
from plan.models import DeviceRam,DeviceInstallment
from phone.models import Country
from django.conf import settings
# https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=SAR&to_currency=USD&apikey=NBTZKC4BMHQ3JUDL
# result['Realtime Currency Exchange Rate']['5. Exchange Rate']
BASE_API = "https://freegeoip.app/json/"
ALPHA_BASE = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', '')

    return ip


def get_exchange_rate(to_currency,request):

    country = request.session['country']

    from_currency = Country.active_country.values('default_currency').get(country_code=country).get('default_currency')

    if from_currency == to_currency:
        request.session['currency_rate'] = 1
        return 1
    api = "{base}&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}".\
         format(base=ALPHA_BASE, from_currency=from_currency, to_currency=to_currency,
                api_key=settings.ALPHA_CURRENCY_KEY)
    try:
        result = urllib.request.urlopen(api).read()
        result = json.loads(result)
        rate = result['Realtime Currency Exchange Rate']['5. Exchange Rate']
        request.session['currency_rate'] = float(rate)
        return rate
    except:
        return 1


def get_location_info(request):
    try:
        api = "{base}{ip}".format(base=BASE_API, ip=get_client_ip(request))
        result = urllib.request.urlopen(api).read()
        result = json.loads(result)
        return result
    except:
        return None


def get_default_currency(request):
    country_code = None
    curr = None;

    try:
        country_code = request.session['country']
    except AttributeError:
        country_code = "SA"
    try:
        curr =Country.active_country.values('default_currency').get(country_code=country_code).get('default_currency', 'SAR')
    except:
        curr = 'SAR'

    return curr


def get_planphone_count(phone,country):
    return  DeviceInstallment.objects.filter(phone__in=DeviceRam.objects.filter(device_phone=phone)).count()


def get_plandevice_count(device):

    if hasattr(device, "plandevice"):
        return device.plandevice.count()