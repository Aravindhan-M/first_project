from django.db import models
from phone.models import (Phone,Country)
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
# Create your models here.


class Survey(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True,blank=True)
    survey_url = models.CharField(max_length=500, null=True, blank=True)
    active = models.BooleanField(_('is active'), default=False)

    class Meta:
        verbose_name = 'survey'
        verbose_name_plural = 'Manage surveys'
        db_table = 'survey'

    def __str__(self):
        return self.survey_url

class SurveyedUsers(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, blank=True)
    surveyed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL,
        verbose_name=_('surveyed By'))