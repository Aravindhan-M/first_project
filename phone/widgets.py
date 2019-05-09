from collections import OrderedDict
from django.forms import NumberInput, HiddenInput,TextInput
from django.db.models import Count, Max, Min
from .models import Brand,RAM,Phone
from plan.models import PlanPhone


def generate_dict(plan_phone,phone,name):
    if name =='brand':

        brand = list(Brand.objects.values('name').filter(phone__id__in=phone).distinct())
        plan_phone = list(PlanPhone.objects.values('brand').filter(id__in=plan_phone))
        print(brand,"brand")
        print(plan_phone,"plan_phone")

        brands = [data['name'].lower().replace("-", " ") for data in brand if data ]
        plan_phone = [data['brand'].lower().replace("-", " ") for data in plan_phone if data ]
        return list((OrderedDict.fromkeys(plan_phone + brands)))
    if name == 'ram':
        ram = list(RAM.objects.values('ram').filter(phone__id__in=phone).distinct())
        plan_phone = list(PlanPhone.objects.values('device_ram_plan_phone__device_ram').filter(id__in=plan_phone))

        rams = [data['ram'].lower().replace("-", " ") for data in ram if data['ram']!='0' and data['ram'].lower()!='unavailable']
        plan_phone = [str(data['device_ram_plan_phone__device_ram'])+" gb"  for data in plan_phone]
        return list((OrderedDict.fromkeys(plan_phone + rams)))


class PhoneDropDown(HiddenInput):

    template_name = 'widgets/dropdown.html'
    input_type = 'hidden'

    def __init__(self, *args, **kwargs):
        self.plan_phone = kwargs.pop("plan_phone", None)
        self.request = kwargs.pop("request", None)
        self.phone = kwargs.pop("phone", None)
        super(PhoneDropDown, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        drop_down_id = 'select_{id}'.format(id=attrs['id'])

        attrs['class'] = 'phone_form_class'
        attrs['value'] = ""
        context = super().get_context(name, value, attrs)
        context['name'] = name
        context['value'] = value if value else "--select--"
        context['drop_down_id'] = drop_down_id
        context['input_id'] = attrs['id']
        if name == 'order_by':
                context['qs'] = ['lowest price','highest price']

        if name == 'price':
            context['qs'] = ['<100','100-500','500-1000','1000-2000','>2000']

        if self.plan_phone is not None and self.phone is not None and name=='brand':
            context['qs'] = generate_dict(self.plan_phone,self.phone,name)
        if self.plan_phone is not None and self.phone is not None and name=='ram':
            context['qs'] = generate_dict(self.plan_phone,self.phone,name)
        return context


class PhoneSearchListCheckbox(HiddenInput):
    template_name = 'widgets/checkboxlist.html'
    input_type = 'hidden'

    def __init__(self, *args, **kwargs):
        self.qs = kwargs.pop("qs", None)
        self.request = kwargs.pop("request", None)
        super(PhoneSearchListCheckbox, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):

        context = super().get_context(name, value, attrs)
        context['name'] = name
        context['div_id']='{name}_div_{id}'.format(id=attrs['id'],name=name)
        context['a_id'] = '{name}_a_{id}'.format(id=attrs['id'],name=name)
        c = self.request.GET.get('color_div_id_color',None)
        s = self.request.GET.get('store_div_id_store', None)
        m = self.request.GET.get('memory_div_id_memory', None)

        if name=='color':
            if c:
                context['checked'] = 'checked'

            context['qs'] = [{'value':i['colors__color_en'],'count':i['colors__color_en__count']} for i in self.qs.values('colors__color_en').order_by().annotate(Count('colors__color_en')) if i['colors__color_en__count'] > 0]
        if name=='store':
            if s:
                context['checked'] = 'checked'
            context['qs'] = [{'value':i['stores__store_en'],'count':i['stores__store_en__count']} for i in self.qs.values('stores__store_en').order_by().annotate(Count('stores__store_en')) if i['stores__store_en__count'] > 0]

        if name=='memory':
            if m:
                context['checked'] = 'checked'
            context['qs'] = [{'value':i['rams__ram_en'],'count':i['rams__ram_en__count']} for i in self.qs.values('rams__ram_en').order_by().annotate(Count('rams__ram_en')) if i['rams__ram_en__count'] > 0]

        return context


class PhoneSearchPriceRangeFilter(TextInput):
    template_name = 'widgets/phone_price_range_slider.html'
    input_type = 'text'

    def __init__(self, *args, **kwargs):
        self.qs = kwargs.pop("qs", None)
        self.request = kwargs.pop("request", None)
        super(PhoneSearchPriceRangeFilter, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        maximum = Phone.objects.aggregate(Max('price'))
        minimum = Phone.objects.aggregate(Min('price'))
        prices = self.request.GET.get('price', None)
        if prices:
            prices = prices.split("to")
        else:
            prices = [minimum['price__min'],maximum['price__max']]


        attrs['id'] = 'amount'

        context = super().get_context(name, value, attrs)
        context['min_qs'] = int(prices[0])
        context['max_qs'] = int(prices[1])
        context['max'] = maximum
        context['min'] = minimum
        context['attr_id'] = attrs['id']
        return context


class PhoneSearchSortBy(TextInput):
    template_name = 'widgets/phone_sort_by.html'
    input_type = 'hidden'


    def __init__(self, *args, **kwargs):
        self.qs = kwargs.pop("qs", None)
        self.request = kwargs.pop("request", None)
        super(PhoneSearchSortBy, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):

        context = super().get_context(name, value, attrs)
        context['val'] = self.request.GET.get("sort_by",None)

        context['name'] = 'sort_by'
        return context





#
#
#
#
# class RangeSlider(NumberInput):
#     template_name = 'widgets/django_rangeslider.html'
#     input_type = 'range'
#
#     def get_context(self, name, value, attrs):
#         slide_ranger_id = 'dataslider_{name}'.format(name=name)
#         if attrs is None:
#             attrs = dict()
#         attrs['id'] = slide_ranger_id
#         attrs['class'] = 'slider plan_form_class'
#         if name == 'price_range':
#             attrs['min'] = min(price) if price else 0
#             attrs['max'] = max(price) if price else 0
#         else:
#             attrs['min'] = '0'
#             attrs['max'] = '100'
#         attrs['value'] = '0'
#
#         context = super().get_context(name, value, attrs)
#         context['widget']['slide_ranger_id'] = slide_ranger_id
#         context['widget']['name'] = name
#         return context
