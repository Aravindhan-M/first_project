from django.db import models
from django.utils.translation import ugettext_lazy as _
class Adpage(models.Model):
    class Meta:
        verbose_name = _('Advertisement Page')
        verbose_name_plural = _('Advertisement Pages')
