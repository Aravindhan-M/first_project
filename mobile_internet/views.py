import json

from django.views.generic import DetailView,TemplateView
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.http import JsonResponse

from el_pagination.views import AjaxListView

from plan.views import PlanView, PlanDetailView
from plan.models import Plan,PlanDevice,DeviceInstallment
from plan.utils import get_device_image_path,donut_calculation_plan_detail
from utils.util import get_plandevice_count
from homepage.utils import get_context_obj

from .forms import MobileInternetForm


class MoboileInternetHome(TemplateView):
    template_name = 'planbaker_06.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_class'] = MobileInternetForm()
        con = get_context_obj(self.request)
        context['obj'] = con['obj']
        context['country'] = con['country']

        return context


class MobileInternetList(PlanView):
    template_name = 'mobile_internet/mobile_internet_home.html'
    page_template = 'mobile_internet/mobile_internet_home_list.html'

    def __init__(self):
        self.form_class = None

        super(MobileInternetList, self).__init__()

    def get_queryset(self):
        sort = self.request.GET.get("order_by")
        # data_range=self.form_class['data'].value()
        price_range = self.request.GET.get('price_range')
        selected_network = self.request.GET.get('selected_network')
        pay_type = self.request.GET.get("pay_type")

        qs = Plan.mobile_internet_objects.all()

        if price_range:
            qs = qs.filter(Q(fee__gte=price_range))

        if selected_network:
            qs = qs.filter(operator_id__operator=selected_network)

        if sort:
            qs = self.sorting(sort=sort, qs=qs, model=self.model)
        self.form_class = MobileInternetForm(self.request.GET, qs=qs, session=self.request.session)
        if pay_type:
            qs = qs.filter(pay_type__exact=pay_type)
        return qs

    # def get(self, request, *args, **kwagrs):
    #     self.form_class = MobileInternetForm(request.GET)
    #     return super(PlanView, self).get(request, *args, **kwagrs)


class MobileInternetDetail(PlanDetailView):
    template_name = 'mobile_internet/mobile_internet_detail.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        phone = None
        add_device = None
        try:

            device_installment = DeviceInstallment.objects.get(plan__slug=kwargs['object'].slug)
        except ObjectDoesNotExist:
            device_installment = None
        except MultipleObjectsReturned:
            device_installment = DeviceInstallment.objects.filter(plan__slug=kwargs['object'].slug)[0]
        except:
            device_installment = None
        if device_installment:

            phone = device_installment.phone.device_phone
            add_device = device_installment.plan_device.all()
            print(add_device,"")
        if phone:
            context['pl_phone'] = phone
            context['pl_image'] = phone.planphoneimages.all()[0].image
        if add_device:

            context['add_device'] = add_device
        con = get_context_obj(self.request)
        context['obj'] = con['obj']
        context['country'] = con['country']

        return donut_calculation_plan_detail(self.get_queryset(),context)


def internet_devices(request):
    context={}
    phones_data = []
    device_list = PlanDevice.objects.all()
    page = request.GET.get('page',1)
    search_query= request.GET.get('query')
    if search_query:
        device_list=device_list.filter(name__icontains=search_query)

    paginator = Paginator(device_list,24)
    try:
        devices = paginator.page(page)
    except PageNotAnInteger:
        devices = paginator.page(paginator.num_pages)

    for device in devices:
        con = {}
        con['name'] = device.name
        con['slug'] = str(device.id)
        con['image'] = get_device_image_path(device)
        con['plancount'] = get_plandevice_count(device)
        if con['plancount']:
            phones_data.append(con)
        else:
            continue
    context['phones'] = phones_data
    data = json.dumps(context)

    return JsonResponse(data, status=200, safe=False)