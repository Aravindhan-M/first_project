from django.http import JsonResponse
from django.views.generic import DetailView,TemplateView
from plan.views import PlanDetailView,PlanView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q,Max

from homepage.utils import get_context_obj
from .models import FixedInternet
from .forms import FixedInternetForm
from .utils import donut_calculation


class FixedInternetHome(TemplateView):
    template_name = 'fixed_internet/fixed_internet_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_class'] = FixedInternetForm()
        con = get_context_obj(self.request)
        context['obj'] = con['obj']
        context['country'] = con['country']
        return context


class FixedInternetList(PlanView):
    model = FixedInternet
    context_object_name = 'plans'
    template_name = 'fixed_internet/fixed_internet_listing.html'
    page_template = 'fixed_internet/fixed_internet_listing_template.html'

    def __init__(self):
        self.form_class = None

        super(FixedInternetList, self).__init__()

    def get_queryset(self):
        sort = self.request.GET.get("order_by")

        data_range = self.request.GET.get('data')
        price_range = self.request.GET.get('price_range')
        selected_network = self.request.GET.get('selected_network')
        try:
            country = self.request.session.get('country')
        except:
            country = "SA"
        #
        qs = FixedInternet.active_fixed_internet.all()
        qs = qs.filter(country__country_code=country)


        if data_range:
             qs = qs.filter(Q(upload_speed__gte=int(data_range)))
        # #
        if price_range:
            qs = qs.filter(Q(monthly_fee__gte=int(price_range)))
        # #
        # if selected_network:
        #
        #     qs = qs.filter(operator_id__operator=selected_network)
        # #
        # if sort:
        #     qs = qs.order_by(sort)

        self.form_class = FixedInternetForm(self.request.GET, qs=qs,session = self.request.session)
        return qs


    def get(self, request, *args, **kwagrs):

        return super(FixedInternetList, self).get(request, *args, **kwagrs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = get_context_obj(self.request)
        context['obj'] = con['obj']
        context['country'] = con['country']
        context['form_class'] = self.form_class
        return donut_calculation(context)


class FixedInternetDetail(DetailView):
    template_name = 'fixed_internet/fixed_internet_detail.html'
    model = FixedInternet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = get_context_obj(self.request)
        context['obj'] = con['obj']
        context['country'] = con['country']
        return context


def fixed_count(request):
    """
    :param request: only_sim=on&phone_name=samsung1&phone_media=&phone_slug=&data=0&minutes=21&messages=0&
    selected_network=
    :return: count of plan
    """

    data = request.GET.get('data', None)

    selected_network = request.GET.get('selected_network', None)
    try:
        country = request.session.get('country')
    except:
        country = "SA"

    qs = FixedInternet.active_fixed_internet.all()
    qs = qs.filter(country__country_code=country)

    if selected_network:
        qs = qs.filter(operator_id__operator=selected_network)

    if data:
        qs = qs.filter(Q(download_speed__gte=int(data)))

    return JsonResponse(qs.count(), status=200, safe=False)