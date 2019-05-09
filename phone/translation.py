from modeltranslation.translator import register, TranslationOptions
from .models import (Phone, PhoneAttribute, AdditionPhoneAttribute, Brand, Color, Store,RAM)


@register(Phone)
class PhoneTranslationOptions(TranslationOptions):
    fields = ('name', 'title','description','price_notes','currency_code','model','product_url')


@register(PhoneAttribute)
class PhoneAttributeTranslationOptions(TranslationOptions):
    fields = ('color', 'ram','max_memory_card_size','max_memory_card','music_playback_time','video_playback_time',
              'standby_talk_time','display_size','display_color','resolution','pixel_density','generation','bluetooth',
              'wifi_features','volte','usb_connectivity','sim_slot','sim_size','tracking_system','processor')


@register(AdditionPhoneAttribute)
class AdditionPhoneAttributeTranslationOptions(TranslationOptions):
    fields = ('attribute_name', 'attribute_value')


@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(RAM)
class RAMTranslationOptions(TranslationOptions):
    fields = ('ram', )


@register(Color)
class ColorTranslationOptions(TranslationOptions):
    fields = ('color', )


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store', )

# @register(Brand)
# class BrandTranslationOptions(TranslationOptions):
#     fields = ('name', 'description')

