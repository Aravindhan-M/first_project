from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


User = settings.AUTH_USER_MODEL
# from utils.util import  get_client_ip
# Create your models here.


class Marketing(models.Model):

    end_user = models.CharField(
        verbose_name=_('End User'), max_length=255)
    user_ip = models.GenericIPAddressField(
        verbose_name=_('User IP Address'), null=True, blank=True)
    user_session = models.CharField(
        verbose_name=_('User Session ID'),
        max_length=40, null=True, blank=True)
    product_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField()
    product_object = GenericForeignKey('product_type','product_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed on %s" %(self.product_object,self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = _('Product Viewed')
        verbose_name_plural = _('Products Viewed')
