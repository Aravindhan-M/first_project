from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Pages(models.Model):
    """ A Model for our Advertiser.  """
    PHONE = 'Phone'
    PLAN = 'Plan'
    MOBILE_PLAN = 'MobilePlan'
    PAGES = (
        (PHONE, 'Phone'),
        (PLAN, 'Plan'),
        (MOBILE_PLAN, 'MobilePlan'),
    )
    page = models.CharField(max_length=12, choices=PAGES, default=PHONE, verbose_name=_('Page'))

    def __str__(self):
        return self.page

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')