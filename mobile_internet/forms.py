from django import forms
from .widgets import RangeSlider
from plan.forms import PlanForm

# <input type="range" min="0" max="100" value="0" class="slider" id="msgRange">


class MobileInternetForm(PlanForm):

    def __init__(self, *args, **kwargs):
        super(MobileInternetForm, self).__init__(*args, **kwargs)
    phone_name = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'plan_form_class','id': 'selected_phone_name_id','value' : ""}))
    phone_slug = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'plan_form_class','id': 'selected_phone_slug_id','value' : ""}))
    phone_media = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'plan_form_class','id': 'selected_phone_media_id','value' : ""}))
    selected_network = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'plan_form_class','id': 'selected_network_id', 'value': ""}))
    order_by = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'plan_form_class', 'id': 'sorting_id', 'value': "","display_val":"Sort By"}))
    # messages = forms.IntegerField(widget=RangeSlider())

    # only_sim = forms.BooleanField(required=False,widget=forms.CheckboxInput())
