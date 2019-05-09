from django.conf import settings
from appconf import AppConf
from django.utils.translation import ugettext_lazy as _


gettext = lambda s: s


class AdsConf(AppConf):

    class Meta:
        prefix = 'ads'



    ZONES = {
        'header': {
            'name': gettext('Header'),
            'ad_size': {
                'xs': '720x150',
                'sm': '375x50',
                'md': '414x736',
                'lg': '800x90'
            },

        },
        'content': {
            'name': gettext('Content'),
            'ad_size': {
                'xs': '720x150',
                'sm': '375x50',
                'md': '414x736',
                'lg': '800x90'
            },

        },
        'sidebar': {
            'name': gettext('Sidebar'),
            'ad_size': {
                'xs': '720x150',
                'sm': '375x50',
                'md': '414x736',
                'lg': '800x90'
            }
        }
    }

    DEFAULT_AD_SIZE = '720x150'

    DEVICES = (
        ('xs', _('720x150')),
        ('sm', _('375x50')),
        ('md', _('414x736')),
        ('lg', _('800x90'))
    )
    ADS_PAGES = ('plan', 'mobileplans', 'phones', 'adsl', 'register','operators')


    ADS_ZONES = {
        'zone1': {
            'name': gettext('zone1'),
            'ad_size': {
                'xs': '720x150',
                'sm': '375x50',
                'md': '414x736',
                'lg': '800x90'
            }

        },
        'zone2': {
            'name': gettext('zone2'),
            'ad_size': {
                'xs': '720x150',
                'sm': '375x50',
                'md': '414x736',
                'lg': '800x90'
            }
        },
        'zone3': {
            'name': gettext('zone3'),
            'ad_size': {
                'xs': '720x150',
                'sm': '375x50',
                'md': '414x736',
                'lg': '800x90'
            }
        },
        'zone4': {
            'name': gettext('zone4'),
            'ad_size': {
                'xs': '720x150',
                'sm': '375x50',
                'md': '414x736',
                'lg': '800x90'
            }

        }
    }

