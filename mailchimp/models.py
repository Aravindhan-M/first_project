from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator,MaxValueValidator
from .utils import MailChimpUtils
from advertisement.models import Ad
from datetime import datetime, timedelta
# Create your models here.


class MailChimp(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True)
    mailchimp_msg = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = _('Mail Campaign')
        verbose_name_plural = _('Mail Campaign')


class EmailScheduler(models.Model):
    advertisement = models.OneToOneField(Ad, on_delete=models.CASCADE, verbose_name=_("Advertisement"))
    sheduled_start = models.DateTimeField(verbose_name=_('Alert Scheduled From'))
    frequency =  models.IntegerField(
        verbose_name=_('Frequency'),
        help_text=_('No of mail per day to Advertisers '
                    'related to one advertisement .'),
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(3)])

    class Meta:
        verbose_name = _('Scheduler')
        verbose_name_plural = _('Email Schedulers')


class Mail():
    pass


def emailscheduler_receiver(sender,instance,created,*args,**kwargs):
    if created:
        EmailScheduler.objects.get_or_create(advertisement = instance,sheduled_start = instance.publication_date_end - timedelta(days= 6))
        print(instance.publication_date_end -timedelta(days= 6))


post_save.connect(emailscheduler_receiver,sender=Ad)


def mailchimp_update_receiver(sender,instance,created,*args,**kwargs):
    pass
    #status_code , response_data = MailChimpUtils().add_email(instance.user.email)


post_save.connect(mailchimp_update_receiver,sender=MailChimp)


def mailchimp_receiver(sender,instance,created,*args,**kwargs):
    if created:
        MailChimp.objects.get_or_create(user=instance)


post_save.connect(mailchimp_receiver,sender=settings.AUTH_USER_MODEL)


