import json
from itertools import chain

from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Q

from el_pagination.views import AjaxListView

from plan.forms import PlanForm
from plan.models import PlanPhone,PhoneContent,DeviceInstallment
from utils.util import get_planphone_count
from homepage.utils import get_context_obj

from .models import Phone,Country
from .utils import refine_internal, get_image_path, get_planphoneimage_path, get_number, group_phone
from .forms import PhoneForm


# class PhoneHomePage(ListView):
#     model = PhoneContent
#     paginate_by = 40
#     template_name = 'phone/phone_mobile.html'
#
#     def __init__(self):
#         self.form_class = None
#
#         super(PhoneHomePage, self).__init__()
#
#     def get_queryset(self):
#         country = self.request.session.get('country', 'SA')
#         plan_phone = DeviceInstallment.objects.values('phone__device_phone__id').filter(country__country_code=country)\
#             .distinct()
#         phone = Phone.objects.values('id').filter(country__country_code=country).distinct('title_tst')
#
#         self.form_class = PhoneForm(plan_phone=plan_phone, phone=phone,request = self.request)
#
#         return PhoneContent.objects.filter(Q(object_id__in=plan_phone, content_type__model='planphone')
#                                            | Q(object_id__in=phone, content_type__model='phone'))\
#             .order_by('-content_type_id')
#
#     def get_context_data(self, **kwargs):
#
#         context = super().get_context_data(**kwargs)
#
#         con = get_context_obj(self.request)
#         context['obj'] = con['obj']
#         context['country'] = con['country']
#
#         context['form_class'] = self.form_class
#         return context


class PhoneHomePage(AjaxListView):
    model = PhoneContent

    template_name = 'phone/phone_mobile.html'
    page_template = 'phone/phone_mobile_list.html'

    def __init__(self):
        self.buy_mobile = []
        self.form_class = None

        super(PhoneHomePage, self).__init__()

    def get_queryset(self):
        i=[]
        # ids =Phone.objects.order_by('title_tst','-price').distinct('title_tst').values_list('id')
        # Phone.objects.filter(id__in=ids).order_by('-price').values('price')
        ram = self.request.GET.get("ram")
        price = self.request.GET.get("price")
        brand = self.request.GET.get("brand")
        order_by = self.request.GET.get("order_by")
        search_field = self.request.GET.get("search_field")
        country = self.request.session.get('country', 'SA')

        if order_by:
            if 'highest' in order_by:

                plan_phone_id = DeviceInstallment.objects.order_by('-phone__device_phone__price').\
                    filter(country__country_code=country).values('phone__device_phone__id').distinct()
                plan_phone = DeviceInstallment.objects.filter(phone__device_phone__id__in=plan_phone_id).\
                    order_by('-phone__device_phone__price').values('phone__device_phone__id',
                                                                   'phone__device_phone__name')
                ids = Phone.objects.order_by('title_tst','-price').filter(country__country_code=country)\
                    .distinct('title_tst').values('id')
                phone = Phone.objects.filter(id__in=ids).order_by('-price').values('id', 'title_tst')
                i =[id['phone__device_phone__id'] for id in plan_phone]+[id['id'] for id in phone]
            else:
                plan_phone_id = DeviceInstallment.objects.order_by('phone__device_phone__price'). \
                    filter(country__country_code=country).values('phone__device_phone__id').distinct()
                plan_phone = DeviceInstallment.objects.filter(phone__device_phone__id__in=plan_phone_id). \
                    order_by('phone__device_phone__price').values('phone__device_phone__id')
                ids = Phone.objects.order_by('title_tst', 'price').filter(country__country_code=country) \
                    .distinct('title_tst').values('id')
                phone = Phone.objects.filter(id__in=ids).order_by('price').values('id')
                i = [id['phone__device_phone__id'] for id in plan_phone] + [id['id'] for id in phone]




        else:
            plan_phone = DeviceInstallment.objects.values('phone__device_phone__id','phone__device_phone__name')\
                .filter(country__country_code=country).distinct()
            phone = Phone.objects.values('id', 'title_tst').filter(country__country_code=country).distinct('title_tst')
        if search_field:
            plan_phone =plan_phone.filter(phone__device_phone__name__search = search_field)
            phone =phone.filter(name__search = search_field)

        if brand:
            plan_phone = plan_phone.filter(phone__device_phone__brand__search=brand)
            phone = phone.filter(brands__name__search=brand)

        if ram:
            plan_phone = plan_phone.filter(phone__device_phone__device_ram_plan_phone__device_ram=get_number(ram)[0])
            phone = phone.filter(rams__ram__search=ram)

        if price:
            price_list = get_number(price)
            if '>' in price:
                plan_phone = plan_phone.filter(phone__device_phone__price__gt=price_list[0])
                phone = phone.filter(price__gt=price_list[0])
            if '-' in price:
                plan_phone = plan_phone.filter(phone__device_phone__price__gte=price_list[0],
                                               phone__device_phone__price__lte=price_list[1])
                phone = phone.filter(price__gte=price_list[0], price__lte=price_list[1])
            if '<' in price:
                plan_phone = plan_phone.filter(phone__device_phone__price__lt=price_list[0])
                phone = phone.filter(price__lt=price_list[0])

        phone, plan_phone, self.buy_mobile = group_phone(plan_phone=plan_phone, phone=phone)

        self.form_class = PhoneForm(self.request.GET, plan_phone=plan_phone, phone=phone, request=self.request)

        if order_by:

            pk_name = ('id' if not getattr(PhoneContent._meta, 'pk', None)
                       else PhoneContent._meta.pk.attname)
            pk_name = '%s.%s' % (PhoneContent._meta.db_table, pk_name)
            clauses = ' '.join(['WHEN %s=%s THEN %s' % (pk_name, pk, i) for i, pk in enumerate(i)])
            print(clauses,"clauses")
            ordering = 'CASE %s END' % clauses
            return PhoneContent.objects.filter(
                Q(object_id__in=plan_phone, content_type__model='planphone')
                | Q(object_id__in=phone, content_type__model='phone')).extra(
                    select={'ordering': ordering}, order_by=('ordering',))

        return PhoneContent.objects.filter(Q(object_id__in=plan_phone, content_type__model='planphone')
                                           | Q(object_id__in=phone, content_type__model='phone'))\
            .order_by('-content_type_id')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        con = get_context_obj(self.request)
        context['obj'] = con['obj']
        context['country'] = con['country']
        context['buy_mobile'] = self.buy_mobile

        context['form_class'] = self.form_class
        print(context)
        return context


def ajaxresult(request):
    context={

    }
    phonesdata = []

    pagination = {

    }
    search = request.GET.get('search_field')
    if search:

        phone_list1 = PhoneContent.objects.filter(object_id__in=PlanPhone.objects.filter(name__icontains=search).values('id'))
        phone_list2 = PhoneContent.objects.filter(
            object_id__in=Phone.objects.filter(name__icontains=search).values('id'))
        phone_list = list(chain(phone_list1, phone_list2))
    else:
        phone_list = PhoneContent.objects.all()
    page = request.GET.get('page',1)
    print(phone_list)
    print("pageno")
    print(page)
    paginator = Paginator(phone_list,24)
    try:
        phones = paginator.page(page)
        pagination['has_next'] = phones.has_next()
        pagination['next_page_number'] = phones.next_page_number()
        pagination['searchq'] = request.GET.get('q')
    except PageNotAnInteger:
        phones = paginator.page(paginator.num_pages)

    for phone in phones:

        con = {}
        con['name'] = phone.content_object.name
        con['slug'] = phone.content_object.slug
        if isinstance(phone.content_object, PlanPhone):
            con['image'] = get_planphoneimage_path(phone.content_object)
        else:
            con['image'] = get_image_path(phone.content_object)
        if isinstance(phone.content_object,PlanPhone):
            c = get_planphone_count(phone.content_object,"SA")
            print("printing c",c)
            if c:
                con['plancount'] = c
        phonesdata.append(con)
    context['phones'] = phonesdata
    context['pagination'] = pagination
    data = json.dumps(context)
    print(context)

    print(data)
    return JsonResponse(data,status=200,safe=False)


class PhoneView(ListView):
    model = Phone
    paginate_by = 2

    def get_queryset(self):

        return Phone.objects.values('name','slug')[10:]

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse(queryset, status=200, safe=False)


class PhoneMobileView(ListView):
    model = Phone
    paginate_by = 20
    context_object_name = 'phones'
    template_name = 'phone/phone_mobile.html'

    def get_queryset(self):
        request = self.request

        # return getlist(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['next'] = self.request.META.get('HTTP_REFERER')
        context['count'] = self.get_queryset().count()
        context['categories'] = ['Mobiles']
        context['stores'] = ['Lulu']
        # context['colors'] = self.get_queryset().values_list("color",flat=True).distinct()
        context['internals'] = refine_internal(list(self.get_queryset().values_list("internal",flat=True).distinct()))
        return context


class AjaxTemplateMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
            print("template nme")
            print(self.ajax_template_name)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)


class PhoneViewAjax(AjaxTemplateMixin,ListView):
    model = Phone
    paginate_by = 40
    context_object_name = 'testphones'
    template_name = 'phone/test_app.html'
    #success_url = reverse_lazy('home')


class MobileView(AjaxTemplateMixin,DetailView):
    model = Phone
    context_object_name = 'details'

    template_name = 'phone/test_app.html'
    #success_url = reverse_lazy('home')


def query_currency_country(request):
    slug = request.GET.get('slug')
    print(slug,"someid")
    if request.is_ajax():
        try:
            country = Country.active_country.get(slug=slug)
            print(country,"countrys")
            return HttpResponse(country.default_currency)
        except Country.DoesNotExist:
            return HttpResponse(serializers.serialize('json', 'Teacher does not exist.'))
        else:
            return HttpResponse("SAR")
    else:
        raise Http404


