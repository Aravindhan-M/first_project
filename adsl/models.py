from django.db import models
from phone.models import (Country)
# Create your models here.
# Paytype
# Linetype
# Monthly payment
# Payment Note
# UpfrontPaymentOptionfor3months
# UpfrontPaymentOptionfor6months
# UpfrontPaymentOptionfor12months
# Downloadspeed
# Uploadspeed
# Months
# Free months
# Benefits
# country_id
# english_url
# arabic_url

class adsl(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    pay_type = models.CharField(max_length=10,blank=True,null=True)
    line_type = models.CharField(max_length=10,blank=True,null=True)
    monthly_payment = models.CharField(max_length=10,blank=True,null=True)
    payment_note = models.CharField(max_length=10,blank=True,null=True)
    upfront_payment_option_for_three_month = models.CharField(max_length=10,blank=True,null=True)
    upfront_payment_option_for_six_month = models.CharField(max_length=10,blank=True,null=True)
    upfront_payment_option_for_twelve_month = models.CharField(max_length=10,blank=True,null=True)
    download_speed = models.CharField(max_length=10,blank=True,null=True)
    upload_speed = models.CharField(max_length=10,blank=True,null=True)
    months = models.IntegerField(blank=True,null=True)
    free_months =  models.IntegerField(blank=True,null=True)
    benefits =  models.CharField(max_length=10,blank=True,null=True)
    english_url =  models.CharField(max_length=500,blank=True,null=True)
    arabic_url =  models.CharField(max_length=500,blank=True,null=True)


    class Meta:
        verbose_name = "ADSL plan"
        verbose_name_plural = "ADSL plans"
        db_table = 'adsl'


    def __str__(self):
        return self.pay_type + ": ADSL"
