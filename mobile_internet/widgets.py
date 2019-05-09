from django.forms import NumberInput
from plan.models import Plan
from django.db.models import Max, Min
plan = Plan.objects.filter(is_active=True, line_type__exact='internet')
# <input type="range" min="0" max="100" value="0" class="slider" id="msgRange">


class RangeSlider(NumberInput):
    template_name = 'widgets/django_rangeslider.html'
    input_type = 'range'

    def get_context(self, name, value, attrs):


        slide_ranger_id = 'dataslider_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['id'] = slide_ranger_id
        attrs['class'] = 'slider mobile_form_class'

        if name == 'price_range':
            print("comes here")
            print(plan.aggregate(Min('fee'))['fee__min'])
            print(plan.aggregate(Max('fee'))['fee__max'])
            attrs['min'] = plan.aggregate(Min('fee'))['fee__min']
            attrs['max'] = plan.aggregate(Max('fee'))['fee__max']
        else:
            attrs['min'] = '0'
            attrs['max'] = '100'

        attrs['value'] = '0'

        context = super().get_context(name, value, attrs)
        context['widget']['slide_ranger_id'] = slide_ranger_id
        context['widget']['name'] = name
        print("printing context")
        print(context)
        return context
