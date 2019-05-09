from django import forms
from django.core.exceptions import ValidationError
from plan.forms import PlanForm
from .models import FixedInternet


class FixedInternetForm(PlanForm):
    pass
    # def __init__(self, *args, **kwargs):
    #
    #     super(FixedInternetForm, self).__init__(*args, **kwargs)
    # phone_name = forms.CharField(widget=forms.HiddenInput(attrs=
    # {'class': 'mobile_form_class','id': 'selected_phone_name_id','value' : ""}))
    # phone_slug = forms.CharField(widget=forms.HiddenInput
    # (attrs={'class': 'mobile_form_class','id': 'selected_phone_slug_id','value' : ""}))
    # phone_media = forms.CharField(widget=forms.HiddenInput
    # (attrs={'class': 'mobile_form_class','id': 'selected_phone_media_id','value' : ""}))
    # selected_network = forms.CharField(widget=forms.HiddenInput(attrs={'class':
    # 'mobile_form_class','id': 'selected_network_id', 'value': ""}))
    # order_by = forms.CharField(widget=forms.HiddenInput(attrs=
    # {'class': 'mobile_form_class','id': 'sorting_id', 'value': "","display_val":"Sort By"}))
    # pricing = forms.IntegerField(widget=RangeSlider())
    # data = forms.IntegerField(widget=RangeSlider())


class FixedInternetAdminForm(forms.ModelForm):
    class Meta:

        model = FixedInternet
        fields = "__all__"

    def clean_nearest_branch_url(self):
        status = self.cleaned_data['status']
        if status:
            if status == 'branch':
                if not self.cleaned_data['nearest_branch_url']:
                    raise ValidationError("Please enter nearest branch URL")
        return self.cleaned_data['nearest_branch_url']

    def clean_online_url(self):
        status = self.cleaned_data['status']
        if status:
            if status == 'online':
                if not self.cleaned_data['online_url']:
                    raise ValidationError("Please enter But online URL")
        return self.cleaned_data['online_url']
