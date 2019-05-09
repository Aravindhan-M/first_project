from modeltranslation.translator import register, TranslationOptions
from .models import FixedInternet


@register(FixedInternet)
class FixedInternetTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'short_description', 'benefits', 'online_url', 'nearest_branch_url')