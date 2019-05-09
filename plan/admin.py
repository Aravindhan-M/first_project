import pprint
from django.contrib import admin
from django.utils.html import format_html
from .models import *
from .forms import CalculationMethodAdminForm
from django.contrib.sessions.models import Session
#from .decorators import admin_active_country


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
    _session_data.allow_tags=True
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']
    date_hierarchy='expire_date'


admin.site.register(Session, SessionAdmin)


class MessageInline(admin.StackedInline):
    model = Message

    exclude = ['donut_message_val',]

    readonly_fields = ["donut_calc", ]

    def donut_calc(self, obj):
        value = obj.donut_message_val
        return format_html('<b>{value}</b>', value=value
                           )

    donut_calc.short_description = "Donut Value"


class DataInline(admin.StackedInline):
    model = Data
    readonly_fields = ["donut_calc", ]
    exclude = ['donut_data_val']

    def donut_calc(self, obj):
        value = obj.donut_data_val
        return format_html('<b>{value}</b>',value=value
        )
    donut_calc.short_description = "Donut Value"


class CallInline(admin.StackedInline):

    model = Call
    exclude = ['donut_call_val',]
    readonly_fields = ["donut_calc", ]

    def donut_calc(self, obj):
        value = obj.donut_call_val
        return format_html('<b>{value}</b>',value=value
        )
    donut_calc.short_description = "Donut Value"


class MMSInline(admin.TabularInline):
    model = MMS


class InternationalBenefitInline(admin.StackedInline):
    model = InternationalBenefit


class AdditionalBenefitInline(admin.StackedInline):
    model = AdditionalBenefit


class PlanAdditionalAttributeInline(admin.StackedInline):
    model = PlanAdditionalAttribute


class OperatorAdmin(admin.ModelAdmin):
    list_display = ('id','operator')


class PlanPhoneImageInline(admin.TabularInline):
    model = PlanPhoneImage


class PlanPhoneAdditionalAttributeInline(admin.TabularInline):
    model = PlanPhoneAdditionalAttribute


class PlanPhoneDisplayAttributeInline(admin.StackedInline):
    model = PlanPhoneDisplayAttribute


class PlanPhoneCameraAttributeInline(admin.StackedInline):
    model = PlanPhoneCameraAttribute


class PlanPhoneMediaAttributeInline(admin.StackedInline):
    model = PlanPhoneMediaAttribute


class PlanPhonePhysicalAttributeInline(admin.StackedInline):
    model = PlanPhonePhysicalAttribute


class PlanPhoneGeneralAttributeInline(admin.StackedInline):
    model = PlanPhoneGeneralAttribute


class PlanPhoneConnectivityAttributeInline(admin.StackedInline):
    model = PlanPhoneConnectivityAttribute


class PlanPhoneMemoryAttributeInline(admin.StackedInline):
    model = PlanPhoneMediaAttribute


class PlanPhoneMessagingAttributeInline(admin.TabularInline):
    model = PlanPhoneMessagingAttribute


class PlanPhoneAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    inlines = (PlanPhoneImageInline, PlanPhoneAdditionalAttributeInline, PlanPhoneDisplayAttributeInline,
               PlanPhoneCameraAttributeInline, PlanPhoneGeneralAttributeInline, PlanPhoneMemoryAttributeInline
               , PlanPhoneConnectivityAttributeInline, PlanPhoneMessagingAttributeInline)


class PlanAdmin(admin.ModelAdmin):

    list_display = ( 'name','operator_id','line_type','pay_type','status','validity_days'
                    ,'fee','one_time_setup_fee', 'is_active','plan_type')
    inlines = (MessageInline,DataInline,CallInline,MMSInline,InternationalBenefitInline,
               AdditionalBenefitInline,PlanAdditionalAttributeInline)
    list_filter = ('line_type','pay_type','status','plan_type')

    #@admin_active_country
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "country":
            kwargs["queryset"] = Country.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)




    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js',
            'js/plan/plan_form.js',
        )

    # def get_form(self, request, obj=None, change=False, **kwargs):
    #
    #     form = super(PlanAdmin, self).get_form(request, obj, **kwargs)
    #
    #     if obj:
    #
    #         if DeviceInstallment.objects.filter(plan=obj,country=obj.country).exists():
    #
    #             form.base_fields['plan_type'].widget.attrs['style'] = 'visibility:hidden'
    #             form.base_fields['plan_type'].label = \
    #                 format_html('''<span style="color:red"><b>Configured to Device cannot be only sim<b></span>''')
    #     if request.method == 'GET':
    #         if obj:
    #             form.base_fields['operator_id'].queryset = operators.objects.all()
    #         else:
    #             form.base_fields['operator_id'].queryset = operators.objects.none()
    #     # print(operators.objects.filter(country__in=obj.subjects.all()))
    #     # if request.method == 'GET':
    #     #     if obj:
    #     #         form.base_fields['operator_id'].queryset = operators.objects.filter(country__in=obj.subjects.all())
    #     #     else:
    #     #         form.base_fields['subjects'].queryset = operators.objects.none()
    #     return form

    # fieldsets = [
    #     ('Content', {
    #         'fields': ('otp_method',),
    #         'description': '<div class="help">%s</div>' % CONTENT_HELP_TEXT,
    #     }),
    # ]


class DeviceRAMAdmin(admin.ModelAdmin):
    list_display = ('device_ram','device_phone')


    # def get_queryset(self, request):
    #     print("printing user query ")
    #     print(request.user.is_operator)
    #     qs = super(PlanAdmin, self).get_queryset(request)
    #     if request.user.is_operator:
    #         return qs.filter(Q(operator_id__operator__iexact = "Airtel"))
    #     # if request.GET.get('q'):  # (Q(creator=owner) | Q(moderated=False))
    #     #     result_qs = qs.filter(Q(title__icontains=request.GET.get('q')) | Q(url__icontains=request.GET.get('q')))
    #     # else:
    #     #     result_qs = qs
    #
    #     return qs

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if request.user.is_operator:
    #
    #         if db_field.name == "operator_id":
    #             kwargs["queryset"] = operators.objects.filter(operator__in=['Airtel'])
    #         return super().formfield_for_foreignkey(db_field, request, **kwargs)


class DeviceImageInline(admin.StackedInline):
    model = DeviceImage


class PlanDeviceAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    inlines = (DeviceImageInline,)


class BulkUploadAdmin(admin.ModelAdmin):
    model = BulkUpload
    list_display = ('otp_method','mf_method',)
    filter_horizontal = ['plans' ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        plans = obj.plans.all()
        print(plans,"plans")
        for plan in plans:
            ob = Plan.objects.get(pk=plan.pk)
            ob.otp_method = obj.otp_method
            ob.mf_method = obj.mf_method
            ob.save()


class DeviceInstallmentAdmin(admin.ModelAdmin):
    list_display = ('plan','phone','installment_value','device_upfront_otp','commitment_months')
    filter_horizontal = ['plan_device']


    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js',
            'js/plan/device_installment_form.js',
        )

    # def save_model(self, request, obj, form, change):
    #
    #     if not change:
    #
    #
    #         if DeviceInstallment.objects.filter(plan=form.cleaned_data['plan'],
    #                                             country=form.cleaned_data['country'])\
    #                 .filter(phone=form.cleaned_data['phone']).exists():
    #             messages.add_message(request, messages.ERROR, 'Not allowed')
    #             return
    #
    #     super().save_model(request, obj, form, change)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #
    #     if db_field.name == "plan":
    #         kwargs["queryset"] = Plan.objects.filter(plan_type=False)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CalculationMethodAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js',
            'js/plan/ev.js',

        )
    form = CalculationMethodAdminForm
    model = CalculationMethod
    list_display = ('name', 'expression')


admin.site.register(operators, OperatorAdmin)
admin.site.register(BulkUpload, BulkUploadAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(DeviceInstallment, DeviceInstallmentAdmin)
admin.site.register(PlanPhone, PlanPhoneAdmin)
admin.site.register(DeviceRam, DeviceRAMAdmin)
admin.site.register(PlanDevice,PlanDeviceAdmin)
admin.site.register(CalculationMethod, CalculationMethodAdmin)