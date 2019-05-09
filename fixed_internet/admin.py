from django.contrib import admin
from .models import FixedInternet
from .forms import FixedInternetAdminForm
from phone.models import Country
# Register your models here.


class FixedInternetAdmin(admin.ModelAdmin):
    form = FixedInternetAdminForm
    list_display = ('name', 'operator_id', 'country', 'download_speed', 'upload_speed',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "country":
            kwargs["queryset"] = Country.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js',
            'js/plan/plan_form.js',
        )


admin.site.register(FixedInternet, FixedInternetAdmin)
