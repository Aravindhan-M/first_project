from django.contrib import admin
from .models import (Phone,Country,Store,Image,Brand,RAM,Color,AdditionPhoneAttribute,PhoneContent)
from django.contrib.admin import SimpleListFilter

class StoreFilter(SimpleListFilter):
    title = 'stores' # or use _('country') for translated title
    parameter_name = 'stores'

    def lookups(self, request, model_admin):
        stores = set([c.country for c in model_admin.model.objects.all()])
        return [(c.id, c.name) for c in stores] + [
          ('AFRICA', 'AFRICA - ALL')]

    def queryset(self, request, queryset):
        if self.value() == 'AFRICA':
            return queryset.filter(country__continent='Africa')
        if self.value():
            return queryset.filter(country__id__exact=self.value())


class StoreInline(admin.TabularInline):
    model = Store

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class ColorInline(admin.TabularInline):
    model = Color
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class BrandInline(admin.TabularInline):
    model = Brand
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class AdditionalAttributeInline(admin.TabularInline):
    model = AdditionPhoneAttribute
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class RamInline(admin.TabularInline):
    model = RAM
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class ImageInline(admin.TabularInline):
    model = Image
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name','slug', 'title')
    list_filter = (
        'country',)
    inlines = (StoreInline, ColorInline,BrandInline,RamInline,ImageInline,AdditionalAttributeInline)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'currency')

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js',
            'js/country/country-form.js',
        )


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id','store','phone')
    list_filter = ('store',)


class PhoneContentAdmin(admin.ModelAdmin):
    list_display = ('content_type',)
    list_filter = ('content_type',)


admin.site.register(PhoneContent, PhoneContentAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Store, StoreAdmin)
