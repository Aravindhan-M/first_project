from django.contrib import admin
from .models import Pages
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    change_list_template = 'admin/page_custom.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = Pages.objects.all()
        except (AttributeError, KeyError):
            return response
        response.context_data['summary'] = list(
            qs

        )
        print(response.context_data['summary'])
        return response

#
# admin.site.register(Pages, PageAdmin)
