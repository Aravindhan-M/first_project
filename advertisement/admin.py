from __future__ import unicode_literals
from django.db.models import Q

import csv

from django import forms
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib.admin import  helpers

from advertisement.forms import AdImageInlineForm
from advertisement.models import *
from advertisement.utils import get_zones_choices,get_pages_choices


class AdvertiserAdmin(admin.ModelAdmin):
    search_fields = ['company_name', 'website']
    list_display = ['company_name', 'website', 'created_by']
    raw_id_fields = ['created_by']

    def get_changeform_initial_data(self, request):
        """
        Provide initial datas when creating an advertiser.
        """
        get_data = super(AdvertiserAdmin, self).get_changeform_initial_data(request)
        return get_data or {
            'created_by': request.user.pk
        }


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by']
    raw_id_fields = ['created_by']

    def get_changeform_initial_data(self, request):
        """
        Provide initial datas when creating a category.
        """
        get_data = super(CategoryAdmin, self). \
            get_changeform_initial_data(request)
        return get_data or {
            'created_by': request.user.pk
        }


class AdAdminForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        widgets = {
            'zone': forms.Select(choices=get_zones_choices()),
            'page': forms.Select(choices=get_pages_choices())
        }


# class AdImageInline(admin.TabularInline):
#     model = AdImage
#     form = AdImageInlineForm
#     fields = ('device', 'image',)
#     editable_fields = ['image_preview']
#
#     def image_preview(self, obj):
#         print("comes here")
#         print(obj.images.all()[0].image.url)
#         # return format_html("<h1><strong>hello</strong></h1>")
#         return format_html('<img src="{url}" width="100px" height="100px" />'.format(
#             url="https://www.gstatic.com/webp/gallery/1.jpg",
#             width='300px',
#             height='300px',
#         )
#         )


class AdImageInline(admin.TabularInline):
    model = AdImage
    form = AdImageInlineForm

class AdVideoInline(admin.TabularInline):
    model = AdVideo



class AdAdmin(admin.ModelAdmin):
    change_list_template = 'admin/custom_ad.html'
    form = AdAdminForm
    # list_display = [
    #     'title', 'url', 'zone', 'advertiser', 'weight', 'publication_date_end']
    # list_filter = [
    #     'publication_date', 'publication_date_end',
    #     'created_at', 'modified_at']
    search_fields = ['title', 'url']
    actions = ['delete_selected']
    # raw_id_fields = ['advertiser', 'created_by']
    inlines = (AdImageInline, AdVideoInline,)
    # readonly_fields = ["image_preview",]

    def get_queryset(self, request):
        print("printing query ")
        print(request.GET.get('q'))
        qs = super(AdAdmin, self).get_queryset(request)
        if request.GET.get('q'): # (Q(creator=owner) | Q(moderated=False))
            result_qs =  qs.filter(Q(title__icontains=request.GET.get('q')) | Q(url__icontains = request.GET.get('q')))
        else:
            result_qs = qs

        return result_qs

    def image_preview(self, obj):
        print("comes here")
        print(obj.images.all()[0].image.url)

        return format_html('<img src="{url}" width="100px" height="100px" />'.format(
            url=obj.images.all()[0].image.url   ,
            width='300px',
            height='300px',
        )
        )

    def get_changeform_initial_data(self, request):
        """
        Provide initial datas when creating an Ad.
        """
        get_data = super(AdAdmin, self).get_changeform_initial_data(request)
        return get_data or {
            'created_by': request.user.pk
        }

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            ad = self.get_queryset(request)
        except (AttributeError, KeyError):
            return response
        response.context_data['h'] = {
            "zone1" : ["sfs","sfsf"]
        }
        headers = list(zip(*get_pages_choices()))[0];
        response.context_data['headers'] = headers
        response.context_data['zones'] = list(map(lambda x1 : ad.filter(page=x1).distinct('zone').all(),headers))
        map(lambda r: r.update({'check_box': helpers.checkbox.render(helpers.ACTION_CHECKBOX_NAME, r['pk'])}),
            ad)
        response.context_data['data'] = list(
            ad

        )

        return response


class ClickAdmin(admin.ModelAdmin):
    search_fields = ['ad__title', 'source_ip', 'session_id']
    list_display = ['ad', 'click_date', 'source_ip', 'session_id']
    list_filter = ['ad', 'click_date', 'ad__zone']
    date_hierarchy = 'click_date'
    actions = ['download_clicks']


    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super(ClickAdmin, self).get_queryset(request)
        return qs.select_related('ad', 'ad__advertiser')

    def download_clicks(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="clicks.csv"'
        writer = csv.writer(response)
        writer.writerow(('Title',
                         'Advertised URL',
                         'Source IP',
                         'Timestamp',
                         'Advertiser ID',
                         'Advertiser name',
                         'Zone'))
        for click in queryset:
            writer.writerow(((click.ad.title),
                             click.ad.url,
                             click.source_ip,
                             click.click_date.isoformat(),
                             click.ad.advertiser.pk,
                             (click.ad.advertiser.company_name),
                             (click.ad.zone)))
        return response
    download_clicks.short_description = "Download selected Ad Clicks"


class ImpressionAdmin(admin.ModelAdmin):
    search_fields = ['ad__title', 'source_ip', 'session_id']
    list_display = ['ad', 'impression_date', 'source_ip', 'session_id']
    list_filter = ['ad', 'impression_date', 'ad__zone']
    date_hierarchy = 'impression_date'
    actions = ['download_impressions']

    def has_add_permission(self, request):
        return False


    def get_queryset(self, request):
        qs = super(ImpressionAdmin, self).get_queryset(request)
        return qs.select_related('ad', 'ad__advertiser')

    def download_impressions(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="impressions.csv"'
        writer = csv.writer(response)
        writer.writerow(('Title',
                         'Advertised URL',
                         'Source IP',
                         'Timestamp',
                         'Advertiser ID',
                         'Advertiser name',
                         'Zone'))
        for impression in queryset:
            writer.writerow(((impression.ad.title),
                             impression.ad.url,
                             impression.source_ip,
                             impression.impression_date.isoformat(),
                             impression.ad.advertiser.pk,
                             (impression.ad.advertiser.company_name),
                             (impression.ad.zone)))
        return response
    download_impressions.short_description = "Download selected Ad Impressions"


admin.site.register(Advertiser, AdvertiserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Click, ClickAdmin)
admin.site.register(Impression, ImpressionAdmin)
