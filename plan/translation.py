from modeltranslation.translator import register, TranslationOptions
from .models import (Plan,InternationalBenefit,MMS,Subscription,AdditionalBenefit,PlanPhone,PlanDevice)


@register(Plan)
class PlanTranslationOptions(TranslationOptions):
    fields = ('name','website_description','fee_notes',)


@register(InternationalBenefit)
class InternationalBenefitsTranslationOptions(TranslationOptions):
    fields = ('international_roaming_benefit','international_rate_promotions','international_minute_rate',)


@register(MMS)
class MMSTranslationOptions(TranslationOptions):
    fields = ('off_net_mms', 'international_mms_rate',)


@register(Subscription)
class SubscriptionTranslationOptions(TranslationOptions):
    fields = ('subscription_method', 'cancellation_method',)


@register(AdditionalBenefit)
class AdditionalBenefitTranslationOptions(TranslationOptions):
    fields = ('special_number_benefits','welcome_package_benefits','contract_renewal_benefits','benefits',
              'device_discount_benefits','other_benefits')


@register(PlanPhone)
class PlanPhoneTranslationOptions(TranslationOptions):
    fields = ('name','title','brand',)


@register(PlanDevice)
class PlanDeviceTranslationOptions(TranslationOptions):
    fields = ('name','title','brand',)


# @register(AppAccess)
# class AppAccessTranslationOptions(TranslationOptions):
#     fields = ('app_name',)



