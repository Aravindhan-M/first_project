from django.forms import NumberInput, HiddenInput, TextInput
from fixed_internet.models import FixedInternet
from django.db.models import Max, Min
# <input type="range" min="0" max="100" value="0" class="slider" id="msgRange">
from plan.models import Plan
plan = Plan.mobile_plan_objects.all()
internet = Plan.mobile_internet_objects.all()
fixed = FixedInternet.active_fixed_internet.all()


class RangeSlider(NumberInput):
    template_name = 'widgets/django_rangeslider.html'
    input_type = 'range'

    def __init__(self,*args,**kwargs):
        self.only_sim_param = kwargs.pop("only_sim_param")
        price_form = kwargs.pop("price_from")
        if price_form == 'PlanForm':
            self.price_form = plan
        if price_form == 'MobileInternetForm':
            self.price_form = internet
        if price_form == 'FixedInternetForm':
            self.price_form = fixed

        self.session= kwargs.pop("session")
        self.qs = kwargs.pop("qs")
        self.param_data = " GB"

        super(RangeSlider,self).__init__(*args,**kwargs)

    def get_context(self, name, value, attrs):
        slide_ranger_id = 'dataslider_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['id'] = slide_ranger_id

        attrs['style'] = 'cursor:pointer'
        attrs['class'] = 'slider plan_form_class'
        # if name == 'data':
        #     if self.price_form.model is FixedInternet:
        #         self.param_data = ' Kbps'

        if name == 'price_range':

            try:
                country= self.session.get('country',"SA")

                if self.price_form.model is FixedInternet:
                    price = [p.monthly_fee for p in self.price_form.filter(country__country_code=country) if
                             self.price_form]
                else:
                    if self.only_sim_param:
                        price = [p.mf_value_only_sim for p in self.price_form.filter(country__country_code=country,
                                                                                     plan_type=1) if
                                 self.price_form]
                    else:
                        price = [p.mf_value for p in self.price_form.filter(country__country_code=country) if
                                 self.price_form]
            except Exception:

                price = [0, 0]

            attrs['min'] = min(price) if price else 0
            attrs['max'] = max(price) if price else 0

        else:
            attrs['min'] = '0'
            attrs['max'] = '500'

        attrs['value'] = '0'
        context = super().get_context(name, value, attrs)
        context['widget']['slide_ranger_id'] = slide_ranger_id
        context['widget']['name'] = name
        # if name == 'data':
        #     context['data_param'] = self.param_data

        if name == 'price_range':
            context['widget']['rate'] = self.session.get("currency_rate",1)

            context['widget']['currency'] =  self.session.get("currency","SAR")
        return context


class PayTypeFilter(HiddenInput):
    def __init__(self,*args,**kwargs):
        self.qs = kwargs.pop("qs")

        super(PayTypeFilter,self).__init__(*args,**kwargs)
    """
    Prepaid,postpaid filter in plan_home html form

    """
    template_name = 'widgets/pay_type_filter.html'
    input_type = 'hidden'

    def get_context(self, name, value, attrs):
        pay_type_id = "pay_type_filter_id"
        if attrs is None:
            attrs = dict()
        attrs['value'] = ''
        attrs['id'] = pay_type_id
        print(self.__class__.__name__,"finding class")
        attrs['class'] = 'plan_form_class'
        context = super().get_context(name, value, attrs)
        if value:
            context['widget']['val'] = value.capitalize()
        else:
            context['widget']['val'] = 'All'
        context['widget']['pay_type_id'] = pay_type_id
        context['widget']['pay_type'] = {'All': self.qs.count() if self.qs else 0,
                                         'Prepaid': self.qs.filter(pay_type='prepaid').count() if self.qs else 0,
                                         'Postpaid': self.qs.filter(pay_type='postpaid').count() if self.qs else 0}
        return context


class CalculationMethodAdminWidgets(TextInput):
    template_name = 'widgets/admin/calculation_method_admin.html'
    input_type = 'text'

    def get_context(self, name, value, attrs):
        attrs['readonly'] = 'readonly'
        context = super().get_context(name, value, attrs)
        return context


