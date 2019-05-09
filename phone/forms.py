from django import forms

from .widgets import PhoneDropDown, PhoneSearchListCheckbox, PhoneSearchPriceRangeFilter,PhoneSearchSortBy

# <input type="range" min="0" max="100" value="0" class="slider" id="msgRange">


class PhoneForm(forms.Form):

    def __init__(self, *args, **kwargs):
        plan_phone = kwargs.pop("plan_phone", None)
        request = kwargs.pop("request", None)
        phone = kwargs.pop("phone", None)
        super(PhoneForm, self).__init__(*args, **kwargs)
        self.fields['brand'] = forms.CharField(widget=PhoneDropDown(plan_phone=plan_phone, phone=phone,request=request))
        self.fields['ram'] = forms.CharField(widget=PhoneDropDown(plan_phone=plan_phone, phone=phone, request=request))
        self.fields['search_field'] = forms.CharField(widget=forms.TextInput
        (attrs={'class':'phone_form_class form-control','id': 'search_id',
                                                    'value': request.GET.get('search_field',""),'placeholder':"Enter Keywords"}))
        # self.fields['price_range'] = forms.IntegerField(widget=RangeSlider(session=session, qs=qs))
    # search_field = forms.CharField(widget=forms.TextInput(attrs={'class':'phone_form_class form-control','id': 'search_id',
    #                                                              'value': "",'placeholder':"Enter Keywords"}))

    # camera = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'phone_form_class',
    #                                                              'id': 'selected_camera_id', 'value': ""}))
    # price = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'phone_form_class',
    #                                                              'id': 'selected_price_id', 'value': ""}))
    # camera = forms.CharField(widget=PhoneDropDown(plan_phone=None, phone=None,request=None))
    price = forms.CharField(widget=PhoneDropDown(plan_phone=None, phone=None,request=None))
    # brand = forms.CharField(widget=PhoneDropDown())
    order_by = forms.CharField(widget=PhoneDropDown(plan_phone=None, phone=None,request=None))
    # brand = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'phone_form_class',
    #                                                               'id': 'selected_brand_id', 'value': ""}))
    # order_by = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'phone_form_class',
    #                                                         'id': 'selected_order_id', 'value': ""}))


class PhoneSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        qs = kwargs.pop("qs", None)
        request = kwargs.pop("request", None)
        # phone = kwargs.pop("phone", None)
        super(PhoneSearchForm, self).__init__(*args, **kwargs)
        self.fields['store'] = forms.CharField(widget=PhoneSearchListCheckbox(qs = qs,request=request))
        self.fields['color'] = forms.CharField(widget=PhoneSearchListCheckbox(qs = qs,request=request))
        self.fields['memory'] = forms.CharField(widget=PhoneSearchListCheckbox(qs = qs,request=request))
        self.fields['price'] = forms.CharField(widget=PhoneSearchPriceRangeFilter(qs=qs, request=request))
        self.fields['sort_by'] = forms.CharField(widget=PhoneSearchSortBy(qs=qs, request=request))
