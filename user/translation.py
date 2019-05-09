from modeltranslation.translator import register, TranslationOptions
from .models import (User)

@register(User)
class UserTranslationOptions(TranslationOptions):
    fields = ('name', )




