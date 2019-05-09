import json
from django.shortcuts import render
from django.http import HttpResponse
from utils.util import get_exchange_rate
from .utils import *

# Create your views here.

country_obj = Country.active_country.all()


def home_page(request):
    # users = User.objects.all()
    context = get_context_obj(request)
    print(context,"context pri")

    return render(request, "home.html", context)


def update_session(request):
    try:
        country = request.GET.get('session_data')
        if country !="None":
            request.session['country'] = country
            request.session['currency'] = country_obj.values('default_currency').get(country_code=country).get('default_currency','SAR')
        else:
            request.session['country'] = "SA"
    except:
       pass

    return HttpResponse('ok')


def update_currency(request):
    try:

        currency = request.GET.get('session_data')
        if currency !="None":
            request.session['currency'] = currency
            get_exchange_rate(currency,request)
        else:

            request.session['currency'] = "SAR"
    except:
        print("exception")

    return HttpResponse('ok')