from django import forms
from .widgets import RangeSlider,PayTypeFilter,CalculationMethodAdminWidgets
from .models import CalculationMethod


# <input type="range" min="0" max="100" value="0" class="slider" id="msgRange">


class PlanForm(forms.Form):

    def __init__(self, *args, **kwargs):
        only_sim_param = None
        if len(args) > 0:
            try:
                if 'only_sim' in args[0]:
                    only_sim_param = args[0].get('only_sim', None)
            except KeyError:
                pass

        session = kwargs.pop("session",None)
        qs = kwargs.pop("qs",None)
        super(PlanForm,self).__init__(*args,**kwargs)
        self.fields['pay_type'] = forms.CharField(widget=PayTypeFilter(qs=qs))
        self.fields['price_range'] = forms.IntegerField(widget=RangeSlider(session=session,qs=qs,
                                                                           price_from=self.__class__.__name__,
                                                                           only_sim_param=only_sim_param))

    phone_name = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'plan_form_class',
                                                                 'id': 'selected_phone_name_id', 'value': ""}))
    phone_slug = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'plan_form_class',
                                                                 'id': 'selected_phone_slug_id', 'value': ""}))
    phone_media = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'plan_form_class',
                                                                  'id': 'selected_phone_media_id', 'value': ""}))
    selected_network = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'plan_form_class',
                                                                       'id': 'selected_network_id', 'value': ""}))
    order_by = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'plan_form_class',
                                                               'id': 'sorting_id', 'value': "",
                                                               "display_val": "Sort By"}))
    messages = forms.IntegerField(widget=RangeSlider(session=None,qs=None,price_from=None, only_sim_param=None))
    minutes = forms.IntegerField(widget=RangeSlider(session=None,qs=None,price_from=None, only_sim_param=None))
    data = forms.IntegerField(widget=RangeSlider(session=None,qs=None,price_from=None, only_sim_param=None))

    only_sim = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'plan_form_class'}))
    # pay_type = forms.CharField(widget=PayTypeFilter(num))


class CalculationMethodAdminForm(forms.ModelForm):
    class Meta:
        model = CalculationMethod
        fields = "__all__"
        widgets = {
            'expression' :CalculationMethodAdminWidgets
        }



# class CountryForm(forms.ModelForm):
#     class Meta:
#         model = Country
#
#     def clean_featured(self):
#         featuredCount = Country.objects.filter(featured=True).count()
#
#         if featuredCount >= 5 and self.cleaned_data['featured'] is True:
#             raise forms.ValidationError("5 Countries can be featured at most!")
#         return self.cleaned_data['featured']
#

