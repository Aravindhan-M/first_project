from django.contrib import admin

from .models import EmailScheduler,MailChimp


class EmailSchedulerAdmin(admin.ModelAdmin):
    list_display = ('advertisement', 'sheduled_start','get_ad_expire_date','get_frequency','get_email',)
   # actions = ['send_nail']

    def get_ad_expire_date(self, obj):
        return obj.advertisement.publication_date_end

    def get_email(self, obj):
        return obj.advertisement.advertiser.email

    def get_frequency(self,obj):
        return "'"+str(obj.frequency) + "' alert mail per day"

    get_ad_expire_date.short_description = "Advertisement expiring at"
    get_frequency.short_description = "Alert frequency"
    get_email.short_description = "Scheduled Email"


class MailChimpAdmin(admin.ModelAdmin):
    change_list_template = 'admin/custom_campaign.html'

    def has_add_permission(self, request):
        return False

    # def get_ad_expire_date(self, obj):
    #     return obj.advertisement.publication_date_end
    #
    # def get_email(self, obj):
    #     return obj.advertisement.advertiser.email
    #
    # def get_frequency(self,obj):
    #     return "'"+str(obj.frequency) + "' alert mail per day"
    #
    # get_ad_expire_date.short_description = "Advertisement expiring at"
    # get_frequency.short_description = "Alert frequency"
    # get_email.short_description = "Scheduled Email"


admin.site.register(EmailScheduler,EmailSchedulerAdmin)
admin.site.register(MailChimp,MailChimpAdmin)