from django.utils.deprecation import MiddlewareMixin
from homepage.utils import get_context_obj


class TemplateMiddleWare(MiddlewareMixin):

    def process_template_response(self, request, response):
        if 'fixed_internet/fixed_internet_detail.html' in response.template_name:
            currency = " {curr}".format(curr=request.session.get('currency', 'SAR'))

            def replace_value(value):
                if ":currency" in value:
                    return value.replace(":currency", currency)
                if ":data" in value:
                    return value.replace(":data", " Kbps")
                return value

            response.context_data['objects'] = {k: replace_value(v)
                                                for (k, v) in response.context_data['object'].available_data.items()}
        con = get_context_obj(request)
        response.context_data['obj'] = con['obj']
        response.context_data['country'] = con['country']

        return response
