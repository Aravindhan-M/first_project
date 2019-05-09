from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.conf.urls import url
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .models import Survey, SurveyedUsers

User = get_user_model()

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('survey_url','show_firm_url',)
    readonly_fields = ["survey_url_link", "bulk_email"]
    model = Survey
    my_id_for_formfield = None

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.my_id_for_formfield = obj
        return super(SurveyAdmin, self).get_form(request, obj, **kwargs)

    def show_firm_url(self, obj):
        return format_html("<a target = '_blank' href='{url}'>View Response </a>",url=obj.survey_url.replace("?embedded=true",""))

    show_firm_url.short_description = "Response Link"

    def survey_url_link(self, obj):
        return format_html('<a href="https://docs.google.com/forms/u/0/" target="_blank">Click here to create survey</a>'
        )

    def send_bulk_email(self, obj):
        recievers=[]

        obj=self.my_id_for_formfield
        allusers = User.objects.all()
        for user in allusers:
            recievers.append(user.email)
            SurveyedUsers.objects.get_or_create(survey=obj,surveyed_by=user)
        try:
            send_mail(
                'Plan Baker user survey',
                obj.survey_url,
                'planbaker@sayonetech.com',
                recievers,
                fail_silently=False,
            )
        except Exception as e:
            print("email exception", e)

        return HttpResponseRedirect('/admin/survey/survey/'+str(obj.id)+'/')

    def bulk_email(self,obj):
        return format_html('<a class="button" href="{}">SEND BULK EMAIL</a>', reverse('admin:bulk-email'))

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^bulk_email/$',
                self.admin_site.admin_view(self.send_bulk_email),
                name='bulk-email',
            ),
        ]
        return custom_urls + urls


class SurveyedUSersAdmin(admin.ModelAdmin):
    model = SurveyedUsers

admin.site.register(Survey, SurveyAdmin)
admin.site.register(SurveyedUsers,SurveyedUSersAdmin)