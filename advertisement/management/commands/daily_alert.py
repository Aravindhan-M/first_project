from django.core.management.base import BaseCommand
from django.utils import timezone
from mailchimp.models import EmailScheduler
from django.core.mail import send_mail


class Command(BaseCommand):
    help = 'Send Daily alert to advertisers'


    def handle(self, *args, **kwargs):
        now = timezone.now()
        ads = EmailScheduler.objects.filter(advertisement__publication_date_end__gte= now, sheduled_start__lte= now)
        recipts=[]
        for ad in ads:

            try:
                recipts.append(ad.advertisement.advertiser.email)
                send_mail(
                    'Advertisement notification',
                     ad.advertisement.url,
                    'planbaker@sayonetech.com',
                     recipts,)

            except Exception as e:
                print("email exception", e)






