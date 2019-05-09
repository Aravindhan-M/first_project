from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save


from phone.models import Country
from plan.models import operators

from .managers import FixedInternetManager
from .utils import unique_slug_generator,get_available_data
# Create your models here.


class FixedInternet(models.Model):
    STATUS = (

        ("branch", "Go To nearest Branch"),
        ("online", "Buy Online")
    )

    PAYTYPE = (
        ("postpaid", "POSTPAID"),
        ("prepaid", "PREPAID")
    )

    LINETYPE = (
        ("voice", "VOICE"),
        ("internet", "INTERNET")
    )
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE, verbose_name='Country')
    operator_id = models.ForeignKey(operators, on_delete=models.CASCADE, verbose_name='Operator')

    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    pay_type = models.CharField(max_length=50, choices=PAYTYPE, null=True, blank=True, verbose_name=_('pay type'))
    line_type = models.CharField(max_length=50, choices=LINETYPE, null=True, blank=True, verbose_name=_('line type'))
    description = models.TextField(max_length=1000, null=True, blank=True)
    short_description = models.TextField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS, null=True, blank=True, verbose_name=_('e-commerce status'))
    monthly_fee = models.IntegerField(null=True, blank=True, default=0, verbose_name=_('Monthly Fee'))
    fee_notes = models.CharField(max_length=500, null=True, blank=True)
    upfront_payment_per_year = models.IntegerField(null=True, blank=True, verbose_name=_('Upfront payment yearly'))
    upfront_payment_half_yearly = models.IntegerField(null=True, blank=True, verbose_name=_('Upfront payment for 6 months'))
    upfront_payment_quarterly = models.IntegerField(null=True, blank=True, verbose_name=_('Upfront payment for 3 months'))
    download_speed = models.IntegerField(null=True, blank=True, verbose_name=_('Download Speed in KBPS'))
    upload_speed = models.IntegerField(null=True, blank=True, verbose_name=_('Upload Speed in KBPS'))
    data_quota = models.IntegerField(null=True, blank=True, verbose_name=_('Data Quota'))
    benefits = models.TextField(max_length=1000, null=True, blank=True)
    nearest_branch_url = models.CharField(max_length=1000, null=True, blank=True,
                                          verbose_name=_('Go To the Nearest Branch URL'))
    online_url = models.CharField(max_length=1000, null=True, blank=True, verbose_name=_('Buy Online URL'))
    available_for = models.CharField(max_length=150, null=True, blank=True)

    objects = models.Manager()
    active_fixed_internet = FixedInternetManager()

    class Meta:
        verbose_name = 'Fixed Internet Plan'
        verbose_name_plural = 'Fixed Internet Plans'

    def get_absolute_url(self):
        return "/fixed_internet/{slug}".format(slug=self.slug)

    def __str__(self):
        return self.name

    @property
    def available_data(self):
        return get_available_data(self)

    # def clean(self):
    #     status = self.status
    #     if status == "branch":
    #         if not self.nearest_branch_url:
    #             raise ValidationError("Please enter nearest branch URL")
    #     if status == "online":
    #         if not self.online_url:
    #
    #             raise ValidationError("Please enterBuy Online URL")


def fixed_internet_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(fixed_internet_pre_save_receiver, sender=FixedInternet)