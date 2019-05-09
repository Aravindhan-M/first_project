import json
from django.views.generic.list import ListView
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import DetailView, TemplateView
from django.db.models import Q,Count
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.http import JsonResponse
from django.http import HttpResponse, Http404
from django.core import serializers
from el_pagination.views import AjaxListView
from phone.models import Country
from plan.forms import PlanForm
from homepage.utils import get_context_obj
from utils.util import get_planphone_count
from .utils import get_plan_phone_image_path,donut_calculation,donut_calculation_plan_detail
from .models import Plan,PlanPhone,DeviceRam,PlanDevice,operators,DeviceInstallment
from .decorators import sort_plan


class MobilePlanHome(TemplateView):
    template_name = 'plan/mobile_plan_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        con = get_context_obj(self.request)
        context['obj'] = con['obj']
        context['country'] = con['country']

        context['form_class'] = PlanForm()
        return context


# class PlanView(ListView):
#     model = Plan
#     paginate_by = 40
#     context_object_name = 'plans'
#     template_name = 'plan/plan_home.html'
#
#     def __init__(self):
#         self.form_class = None
#
#         super(PlanView, self).__init__()
#
#     def get_queryset(self):
#         sort = self.request.GET.get("order_by")
#         # pay_type = self.form_class['pay_type'].value()
#         # selected_network = self.form_class['selected_network'].value()
#         # price_range = self.form_class['price_range'].value()
#         pay_type = self.request.GET.get("pay_type")
#         selected_network = self.request.GET.get("selected_network")
#         price_range = self.request.GET.get("price_range")
#         data = int(self.request.GET.get("data",0))
#         minutes = int(self.request.GET.get("minutes",0))
#         phone_slug = self.request.GET.get("phone_slug")
#         try:
#             country = self.request.session.get('country')
#         except:
#             country = "SA"
#
#         try:
#             # only_sim = self.form_class['only_sim'].value()
#             only_sim = self.request.GET.get("only_sim")
#             if only_sim:
#                 qs = Plan.mobile_plan_objects.filter(Q(plan_type__exact=1),
#
#                                          Q(data__donut_data_val__gte=data*1000),
#                                          Q(call__donut_call_val__gte=minutes))
#
#             else:
#
#                 qs = Plan.mobile_plan_objects.filter(
#
#                                      Q(data__donut_data_val__gte=data*1000),
#                                      Q(call__donut_call_val__gte=minutes))
#
#
#             # qs.get(donut_message_val__gte = self.form_class['message'].value())
#             # User.objects.filter(userprofile__level__gte=0)
#         except ValueError:
#             qs = Plan.mobile_plan_objects.all()
#         if selected_network:
#             qs = qs.filter(operator_id__operator=selected_network)
#         if price_range:
#
#             qs = qs.filter(id__in=[q.id for q in qs if q.mf_value >= int(price_range)])
#
#         if sort:
#
#             if sort=="fee":
#                 pk_name = ('id' if not getattr(Plan._meta, 'pk', None)
#                            else Plan._meta.pk.attname)
#                 pk_name = '%s.%s' % (Plan._meta.db_table, pk_name)
#                 pk_list = [q.id for q in sorted(qs, key=lambda qs: qs.mf_value)]
#                 clauses = ' '.join(['WHEN %s=%s THEN %s' % (pk_name,pk, i) for i, pk in enumerate(pk_list)])
#                 ordering = 'CASE %s END' % clauses
#                 qs = qs.filter(pk__in=pk_list).extra(
#                     select={'ordering': ordering}, order_by=('ordering',))
#
#             elif sort=="-fee":
#                 pk_name = ('id' if not getattr(Plan._meta, 'pk', None)
#                            else Plan._meta.pk.attname)
#                 pk_name = '%s.%s' % (Plan._meta.db_table, pk_name)
#
#                 pk_list = [q.id for q in sorted(qs, key=lambda qs: qs.mf_value, reverse=True)]
#
#                 clauses = ' '.join(['WHEN %s=%s THEN %s' % (pk_name, pk, i) for i, pk in enumerate(pk_list)])
#                 ordering = 'CASE %s END' % clauses
#                 qs = qs.filter(pk__in=pk_list).extra(
#                     select={'ordering': ordering}, order_by=('ordering',))
#             else:
#                 qs=qs.order_by(sort)
#         if phone_slug and not only_sim:
#             qs = qs.filter(id__in=DeviceInstallment.objects.filter(plan__in=qs,phone__device_phone__id=int(phone_slug)).values('plan'))
#         qs =qs.filter(country__country_code=country)
#
#         self.form_class = PlanForm(self.request.GET, qs=qs,session = self.request.session)
#         if pay_type:
#             qs = qs.filter(pay_type__exact=pay_type)
#
#
#
#
#
#         return qs
#
#     def get(self, request, *args, **kwagrs):
#         return super(PlanView, self).get(request, *args, **kwagrs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         con = get_context_obj(self.request)
#         context['obj'] = con['obj']
#         context['country'] = con['country']
#         context['form_class'] = self.form_class
#
#         return donut_calculation(context)

class PlanView(AjaxListView):
    # model = Plan
    # paginate_by = 40
    # context_object_name = 'plans'
    # template_name = 'plan/plan_home.html'
    model = Plan

    context_object_name = 'plans'
    template_name = 'plan/plan_home.html'
    page_template = 'plan/plan_home_list.html'

    def __init__(self):
        self.form_class = None

        super(PlanView, self).__init__()

    @sort_plan
    def sorting(self,*args,**kwargs):
        return kwargs['qs']

    def get_queryset(self):

        sort = self.request.GET.get("order_by")
        # pay_type = self.form_class['pay_type'].value()
        # selected_network = self.form_class['selected_network'].value()
        # price_range = self.form_class['price_range'].value()
        pay_type = self.request.GET.get("pay_type")
        selected_network = self.request.GET.get("selected_network")
        price_range = self.request.GET.get("price_range")
        data = int(self.request.GET.get("data",0))
        minutes = int(self.request.GET.get("minutes",0))
        phone_slug = self.request.GET.get("phone_slug")
        messages = int(self.request.GET.get("messages",0))
        only_sim = self.request.GET.get("only_sim",None)

        try:
            country = self.request.session.get('country')
        except:
            country = "SA"

        try:
            # only_sim = self.form_class['only_sim'].value()
            qs = Plan.mobile_plan_objects.filter(
                                                 Q(message__donut_message_val__gte=messages),

                                                 Q(data__donut_data_val__gte=data * 1000),
                                                 Q(call__donut_call_val__gte=minutes))

            # if only_sim:
            #     qs = Plan.mobile_plan_objects.filter(Q(plan_type__exact=1),
            #                                          Q(message__donut_message_val__gte=messages),
            #
            #                              Q(data__donut_data_val__gte=data*1000),
            #                              Q(call__donut_call_val__gte=minutes))

        except ValueError:
            qs = Plan.mobile_plan_objects.all()
        if only_sim:
            qs = qs.filter(Q(plan_type__exact=1))
        if selected_network:
            qs = qs.filter(operator_id__operator=selected_network)
        if price_range:

            qs = qs.filter(id__in=[q.id for q in qs if q.mf_value >= int(price_range)])

        if sort:
            qs = self.sorting(sort=sort, qs=qs, model=self.model)

            # if sort=="fee":
            #     pk_name = ('id' if not getattr(Plan._meta, 'pk', None)
            #                else Plan._meta.pk.attname)
            #     pk_name = '%s.%s' % (Plan._meta.db_table, pk_name)
            #     pk_list = [q.id for q in sorted(qs, key=lambda qs: qs.mf_value,reverse=False)]
            #     clauses = ' '.join(['WHEN %s=%s THEN %s' % (pk_name,pk, i) for i, pk in enumerate(pk_list)])
            #     print(clauses,"planclauses")
            #     ordering = 'CASE %s END' % clauses
            #     qs = qs.filter(pk__in=pk_list).extra(
            #         select={'ordering': ordering}, order_by=('ordering',))
            #
            # elif sort=="-fee":
            #     pk_name = ('id' if not getattr(Plan._meta, 'pk', None)
            #                else Plan._meta.pk.attname)
            #     pk_name = '%s.%s' % (Plan._meta.db_table, pk_name)
            #
            #     pk_list = [q.id for q in sorted(qs, key=lambda qs: qs.mf_value, reverse=True)]
            #
            #     clauses = ' '.join(['WHEN %s=%s THEN %s' % (pk_name, pk, i) for i, pk in enumerate(pk_list)])
            #     ordering = 'CASE %s END' % clauses
            #     qs = qs.filter(pk__in=pk_list).extra(
            #         select={'ordering': ordering}, order_by=('ordering',))
            # else:
            #     qs=qs.order_by(sort)
        if phone_slug and not only_sim:
            qs = qs.filter(id__in=DeviceInstallment.objects.filter(plan__in=qs,phone__device_phone__id=int(phone_slug)).values('plan'))
        qs =qs.filter(country__country_code=country)

        self.form_class = PlanForm(self.request.GET, qs=qs,session = self.request.session)
        if pay_type:
            qs = qs.filter(pay_type__exact=pay_type)
        print(qs,"printing qs for plan")
        return qs

    def get(self, request, *args, **kwagrs):
        return super(PlanView, self).get(request, *args, **kwagrs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = get_context_obj(self.request)
        context['obj'] = con['obj']
        context['country'] = con['country']
        context['form_class'] = self.form_class

        return donut_calculation(context)


class PlanDetailView(DetailView):
    template_name = 'plan/plan_detail.html'
    model = Plan

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        phone = None
        add_device = None
        # phone = PlanPhone.objects.filter(deviceram__in=kwargs['object'].device_ram.all()).distinct()


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

        if phone:

            context['pl_phone'] = phone
            context['pl_image'] = phone.planphoneimages.all()[0].image

        # add_device = PlanDevice.objects.filter(plandevice__in=[kwargs['object']])

        if add_device:

            context['add_device'] = add_device
        con = get_context_obj(self.request)
        context['obj'] = con['obj']
        context['country'] = con['country']
        context['max_message_donut'] = self.request.GET.get('message',0)
        context['max_data_donut'] = self.request.GET.get('data',0)
        context['max_call_donut'] = self.request.GET.get('call',0)
        print(context,"ccc")


        return context


def plan_count(request):
    """
    :param request: only_sim=on&phone_name=samsung1&phone_media=&phone_slug=&data=0&minutes=21&messages=0&
    selected_network=
    :return: count of plan
    """
    phone_slug = request.GET.get('phone_slug', '0')
    data = request.GET.get('data', '0')
    minutes = request.GET.get('minutes', '0')
    messages = request.GET.get('messages', '0')
    selected_network = request.GET.get('selected_network', None)
    only_sim = request.GET.get('only_sim', None)
    try:
        country = request.session.get('country')
    except:
        country = "SA"

    qs = Plan.mobile_plan_objects.all()

    if selected_network:
        qs = qs.filter(operator_id__operator=selected_network)
    if data:
        qs = qs.filter(Q(data__donut_data_val__gte=int(data)*1000))
    if minutes:
        qs = qs.filter(Q(call__donut_call_val__gte=int(minutes)))
    if messages:
        qs = qs.filter(Q(message__donut_message_val__gte=int(messages)))

    if only_sim:
        qs =qs.filter(Q(plan_type__exact=1))
    # else:
    #     qs = qs.filter(Q(plan_type__exact=0))
    qs=qs.filter(country__country_code=country)

    if phone_slug:
        qs =DeviceInstallment.objects.filter(plan__in=qs,phone__device_phone__id=int(phone_slug))

    return JsonResponse(qs.count(), status=200, safe=False)


def mobile_internet_count(request):
    """
    :param request: only_sim=on&phone_name=samsung1&phone_media=&phone_slug=&data=0&minutes=21&messages=0&
    selected_network=
    :return: count of plan
    """
    phone_slug = request.GET.get('phone_slug', '0')
    data = request.GET.get('data', '0')

    selected_network = request.GET.get('selected_network', None)

    try:
        country = request.session.get('country')
    except:
        country = "SA"

    qs = Plan.mobile_internet_objects.all()

    if selected_network:
        qs = qs.filter(operator_id__operator=selected_network)
    if data:
        qs = qs.filter(Q(data__donut_data_val__gte=int(data)*1000))

    if phone_slug:
        qs =qs.filter(device_ram__id=int(phone_slug))

    print(qs.count(),"count before mmcountry filter")
    qs=qs.filter(country__country_code=country)
    print(qs.count(),"count agftert mmcountry filter")
    return JsonResponse(qs.count(), status=200, safe=False)


def ajax_result(request):

    context = {}
    phones_data = []
    try:
        country = request.session.get('country')
    except:
        country = "SA"

    phone_list = PlanPhone.objects.filter\
        (id__in=DeviceRam.objects.filter
        (id__in=DeviceInstallment.objects.filter().values('phone')).values('device_phone'))

    page = request.GET.get('page',1)

    paginator = Paginator(phone_list,24)
    try:
        phones = paginator.page(page)
    except PageNotAnInteger:
        phones = paginator.page(paginator.num_pages)





    for phone in phones:
        print(phone,"foir-lp")
        con = {}
        con['name'] = phone.name
        con['slug'] = str(phone.id)
        con['image'] = get_plan_phone_image_path(phone)
        con['plancount'] = get_planphone_count(phone,country)
        phones_data.append(con)
        # if con['plancount']:
        #     phones_data.append(con)
        # else:
        #     continue
    context['phones'] = phones_data
    # context['pagination'] = pagination
    print(context,"context")
    data = json.dumps(context)

    return JsonResponse(data, status=200, safe=False)


class AjaxTemplateMixin(object):
    def dispatch(self, request, *args, **kwargs):

        if kwargs.get('param') == 'image':

            self.ajax_template_name = 'plan/device_gallery.html'

        if request.is_ajax():
            self.template_name = self.ajax_template_name

        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)


class DeviceDetailView(AjaxTemplateMixin, DetailView):
    ajax_template_name = 'plan/device_specs.html'
    model = PlanPhone

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context


def query_operator_country(request):
    id = request.GET.get('id')

    if request.is_ajax():
        try:
            country = Country.active_country.get(id=id)
        except Country.DoesNotExist:
            return HttpResponse(serializers.serialize('json', 'Country does not exist.'))
        else:
            return HttpResponse(serializers.serialize('json',operators.objects.filter(country=country), fields=('id','operator',)))
    else:
        raise Http404


def query_plan_country(request):
    id = request.GET.get('id')


    if request.is_ajax():
        try:
            plan = Plan.objects.filter(plan_type=False, country__id=id)
        except Plan.DoesNotExist:
            print("inside exception")
            return HttpResponse(serializers.serialize('json', 'Plan Does not  exists.'))
        else:
            return HttpResponse(serializers.serialize('json',plan, fields=('id','name',)))
    else:
        raise Http404

def single_object_representation(obj):
    return  {
        'id': obj.id,
        'name': obj.__str__(),

    }



def query_phone_plan_country(request):
    id = request.GET.get('id')
    plan = request.GET.get('plan')
    print(id)
    print(plan)

    if request.is_ajax():
        # try:
        alloted_phone = DeviceInstallment.objects.values('phone').filter(plan__id=plan,country__id=id)
        phone = DeviceRam.objects.exclude(id__in=alloted_phone)
        result = [single_object_representation(obj) for obj in phone]
        print(result,"json reult")

        return JsonResponse(result, safe=False)
    else:
        raise Http404


class PlanPhoneList(AjaxListView):

    context_object_name = "phone_list"
    template_name = "plan/phone_list.html"
    page_template = 'plan/phone_list_page.html'

    def get_queryset(self):
        try:
            country = self.request.session.get('country')
        except:
            country = "SA"

        phone_list = PlanPhone.objects.filter\
            (id__in=DeviceRam.objects.filter
            (id__in=DeviceInstallment.objects.filter(country__country_code=country).values('phone')).values('device_phone'))
        return phone_list


def query_device_installment(request):
    country = request.GET.get('country')
    operator = request.GET.get('operator')
    line = request.GET.get('line')
    print(country)
    print(operator)
    print(line)
    try:

        plan=Plan.objects.filter(is_active=True, line_type=line, operator_id__id=int(operator), country__id=int(country))
    except:
        return HttpResponse(serializers.serialize('json', 'Country does not exist.'))
    else:
        return HttpResponse(
            serializers.serialize('json', plan, fields=('id', 'name',)))
