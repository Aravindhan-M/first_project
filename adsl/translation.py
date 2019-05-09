from modeltranslation.translator import register, TranslationOptions
from .models import (adsl)

@register(adsl)
class adslTranslationOptions(TranslationOptions):
    fields = ('pay_type', 'line_type','monthly_payment','payment_note','benefits')
