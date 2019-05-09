from django.conf import settings
from appconf import AppConf


class ConnekioConf(AppConf):

    END_POINT = 'https://api.connekio.com'

    class Meta:
        prefix = 'SMS'
