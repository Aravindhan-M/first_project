from django.utils.deprecation import MiddlewareMixin
from utils.util import get_location_info,get_default_currency


class IpMiddleWare(MiddlewareMixin):

    def process_request(self, request):

        try:
            request.session['country']

        except Exception:
            info = get_location_info(request)
            if info:

                request.session['country'] = info['country_code']
            else:
                pass
        try:

            request.session['currency']
        except Exception:
            request.session['currency'] = get_default_currency(request)

        return None