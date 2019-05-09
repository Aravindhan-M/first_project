from phone.models import Country
from django.core.exceptions import ObjectDoesNotExist
def get_context_obj(request):
    try:

        session_country = request.session['country']
        obj = Country.active_country.all()
        if session_country!="":

            try:
                country = obj.get(country_code=session_country)
            except ObjectDoesNotExist:
                country = obj.get(country_code="SA")

        else:
            country = obj.get(country_code='SA')
            request.session['country'] = 'SA'
        return {
            "obj" : obj,
            "country" : country
        }
    except:
        pass
