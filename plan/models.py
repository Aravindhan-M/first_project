from __future__ import unicode_literals

from multiselectfield import MultiSelectField
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save,post_save,pre_delete
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from phone.models import PhoneContent,Country
from .utils import *
from .managers import MobilePlanManager,MobileInternetManager
from django.urls import reverse
# Create your models here.


# class PlanPhone(models.Model):
#
#     name =models.CharField(
#         max_length=10, null=True, blank=True, verbose_name=_('SMS To all Networks Rate/SMS after consumption (SAR)'))
#     slug_field =models.CharField(
#         max_length=10, null=True, blank=True, verbose_name=_('SMS To all Networks Rate/SMS after consumption (SAR)'))
#     title =models.CharField(
#         max_length=10, null=True, blank=True, verbose_name=_('SMS To all Networks Rate/SMS after consumption (SAR)'))
#     description =models.CharField(
#         max_length=10, null=True, blank=True, verbose_name=_('SMS To all Networks Rate/SMS after consumption (SAR)'))
#     release_date = models.CharField(
#         max_length=10, null=True, blank=True, verbose_name=_('SMS To all Networks Rate/SMS after consumption (SAR)'))
#
#     created_date =models.CharField(
#         max_length=10, null=True, blank=True, verbose_name=_('SMS To all Networks Rate/SMS after consumption (SAR)'))
#     modified_date =models.CharField(
#         max_length=10, null=True, blank=True, verbose_name=_('SMS To all Networks Rate/SMS after consumption (SAR)'))


class PlanPhone(models.Model):

    name = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    brand = models.CharField(max_length=500,null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    primary_camera = models.IntegerField(null=True, blank=True, verbose_name="Primary Camera")


    # color = models.CharField(max_length=100, null=True, blank=True)
    # internal = models.CharField(max_length=100, null=True, blank=True)
    # external = models.CharField(max_length=100, null=True, blank=True)
    # ram = models.CharField(max_length=100, null=True, blank=True)
    # processor = models.CharField(max_length=100, null=True, blank=True)
    # sim = models.CharField(max_length=100, null=True, blank=True)
    # sim_slot = models.CharField(max_length=100, null=True, blank=True)
    # os = models.CharField(max_length=100, null=True, blank=True)
    # weight = models.CharField(max_length=100, null=True, blank=True)
    # primary_camera = models.CharField(max_length=75, null=True, blank=True)
    # secondary_camera = models.CharField(max_length=75, null=True, blank=True)
    # color = models.CharField(max_length=5, null=True, blank=True)
    # ram = models.CharField(max_length=10, null=True, blank=True)
    # display_size = models.CharField(max_length=10, null=True, blank=True)
    # resolution = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'Phone related to plan'
        verbose_name_plural = 'Phone related to plans'
        db_table = 'planPhone'

    def __str__(self):
        return self.name


def planphone_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(planphone_pre_save_receiver, sender=PlanPhone)


def create_plan_phone(sender, instance, created, **kwargs):
    content_type = ContentType.objects.get_for_model(instance)
    try:
        phone_content = PhoneContent.objects.get(content_type=content_type,
                              object_id=instance.id)
    except PhoneContent.DoesNotExist:
        phone_content = PhoneContent(content_type=content_type, object_id=instance.id)

    phone_content.save()


post_save.connect(create_plan_phone, sender=PlanPhone)


def delete_plan_phone(sender,instance,**kwargs):
    content_type = ContentType.objects.get_for_model(instance)
    try:
        phone_content = PhoneContent.objects.get(content_type=content_type,
                              object_id=instance.id)
    except PhoneContent.DoesNotExist:
        pass

    phone_content.delete()


pre_delete.connect(delete_plan_phone,sender=PlanPhone)


class PlanDevice(models.Model):

    name = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    brand = models.CharField(max_length=500,null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)

    class Meta:
        verbose_name = 'Device related to plan'
        verbose_name_plural = 'Device related to plans'
        db_table = 'planDevice'

    def __str__(self):
        return self.name


def plandevice_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(plandevice_pre_save_receiver, sender=PlanDevice)


class DeviceImage(models.Model):
    plan_device = models.OneToOneField(PlanDevice, on_delete=models.CASCADE, related_name="deviceimage",null=True)
    image = models.ImageField(verbose_name=_('Image'), max_length=255)


class PlanPhoneDisplayAttribute(models.Model):
    planphones = models.OneToOneField(PlanPhone, on_delete=models.CASCADE,null=True, related_name="planphone_display_attr")
    type = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Display Type'))
    size = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Display Size'))
    resolution = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Display Resolution'))
    protection = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Display Protection'))

    class Meta:
        verbose_name = 'PlanPhone Display Attribute'
        verbose_name_plural = 'PlanPhone Display Attributes'
        db_table = 'planphoneadisplayattr'


class PlanPhoneCameraAttribute(models.Model):

    planphones = models.OneToOneField(PlanPhone, null=True,on_delete=models.CASCADE, related_name="planphone_cam_attr")

    features = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Camera Feautures'))
    Video = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Video'))
    rear_camera_quality = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Rear Camera Quality'))
    rear_camera_resolution = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Rear Camera Image Resolution'))
    front_camera_quality = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Front Camera Quality'))
    front_camera_resolution = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Front Camera Image Resolution'))

    class Meta:
        verbose_name = 'PlanPhone Camera Attribute'
        verbose_name_plural = 'PlanPhone Camera Attributes'
        db_table = 'planphonecameraattr'


class PlanPhoneMediaAttribute(models.Model):
    planphones = models.OneToOneField(PlanPhone,null=True, on_delete=models.CASCADE, related_name="planphone_media_attr")
    loudspeaker = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Loudspeaker'))
    jack = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Jack'))

    class Meta:
        verbose_name = 'PlanPhone Media Attribute'
        verbose_name_plural = 'PlanPhone Media Attributes'
        db_table = 'planphonemediaattr'


class PlanPhonePhysicalAttribute(models.Model):
    planphones = models.OneToOneField(PlanPhone,null=True, on_delete=models.CASCADE, related_name="planphone_physical_attr")
    dimensions = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Dimensions'))
    weights = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Weights'))
    build = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Build'))
    sim = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Sim'))

    class Meta:
        verbose_name = 'PlanPhone Physical Attribute'
        verbose_name_plural = 'PlanPhone Physical Attributes'
        db_table = 'planphonephysicalattr'


class PlanPhoneGeneralAttribute(models.Model):
    planphones = models.OneToOneField(PlanPhone,null=True, on_delete=models.CASCADE, related_name="planphone_general_attr")

    released =  models.DateTimeField(
        verbose_name=_('Release Date:'),
        null=True,blank=True)
    color = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Color'))
    price = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Price'))
    battery = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Battery'))
    # os = models.CharField(
    #     max_length=500, null=True, blank=True, verbose_name=_('OS'))
    stand_by = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Battery Stand By Time'))
    os = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('OS'))
    chip_set = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Chip set'))
    cpu = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('CPU'))

    class Meta:
        verbose_name = 'PlanPhone General Attribute'
        verbose_name_plural = 'PlanPhone General Attributes'
        db_table = 'planphonegeneralattr'


class PlanPhoneConnectivityAttribute(models.Model):
    planphones = models.OneToOneField(PlanPhone,null=True, on_delete=models.CASCADE, related_name="planphone_conn_attr")
    bluetooth = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Bluetooth'))
    bluetooth_profile = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Bluetooth profile'))
    wifi = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('WIFI'))
    usb_version = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('USB Version'))
    connecting_features = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Connectivity Features'))
    gps = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('GPS'))

    radio = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('radio'))

    class Meta:
        verbose_name = 'PlanPhone Connectivity Attribute'
        verbose_name_plural = 'PlanPhone Connectivity Attributes'
        db_table = 'planphoneconnattr'


class PlanPhoneMemoryAttribute(models.Model):
    planphones = models.OneToOneField(PlanPhone,null=True, on_delete=models.CASCADE, related_name="planphone_memory_attr")
    card_slot = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Card Slot'))
    internal = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Memory Internal'))
    memory_card_upto = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Memory Card Up to'))

    class Meta:
        verbose_name = 'PlanPhone Memory Attribute'
        verbose_name_plural = 'PlanPhone Memory Attributes'
        db_table = 'planphonememoryattr'


class PlanPhoneMessagingAttribute(models.Model):
    planphone = models.ForeignKey(PlanPhone, on_delete=models.CASCADE, related_name="planphone_messaging_attr")
    attr_name = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Messaging Attribute Name'))
    attr_value = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Messaging Attribute Value'))

    class Meta:
        verbose_name = 'PlanPhone Messaging Attribute'
        verbose_name_plural = 'PlanPhone Messaging Attributes'
        db_table = 'planphonemessagingattr'


class PlanPhoneAdditionalAttribute(models.Model):
    planphone = models.ForeignKey(PlanPhone, on_delete=models.CASCADE, related_name="planphone_add_attr")
    attr_name = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Attribute Name'))
    attr_value = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Attribute Value'))

    class Meta:
        verbose_name = 'PlanPhone Additional Attribute'
        verbose_name_plural = 'PlanPhone Additional Attributes'
        db_table = 'planphoneaddattr'


class PlanPhoneImage(models.Model):
    planphone = models.ForeignKey(
        PlanPhone, on_delete=models.CASCADE, verbose_name=_('Plan Phone Image'),
        related_name='planphoneimages')

    image = models.ImageField(verbose_name=_('Image'), max_length=255)


class DeviceRam(models.Model):
    STORAGE = (("GB", "GB"), ("MB", "MB"), ("NONE", "NONE"))
    device_ram = models.IntegerField(null=True, blank=True, default=0, verbose_name=_('Device RAM'))
    device_phone = models.ForeignKey(PlanPhone, on_delete=models.CASCADE, null=True, verbose_name='Plan Device',
                                     related_name='device_ram_plan_phone')
    storage_capacity = models.CharField(choices=STORAGE, max_length=50, default="NONE", null=True,
                                        verbose_name="Capacity parameter")

    class Meta:
        verbose_name = 'RAM related to plan'
        verbose_name_plural = 'RAM related to plan'

    @property
    def phone_name(self):

        return self.device_phone.name

    def __str__(self):
        if not self.device_ram:
            return "{name}".format(name=self.device_phone.name)
        return "{name} {ram}{capacity}".format(name=self.device_phone.name, ram=self.device_ram,
                                               capacity=self.storage_capacity)


class operators(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    operator = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(verbose_name=_('Operator Logo'), max_length=255,null=True,blank=True)

    class Meta:
        verbose_name = 'operator'
        verbose_name_plural = 'operators'
        db_table = 'operator'

    def __str__(self):
        return self.operator


class CalculationMethod(models.Model):

    name = models.CharField(max_length=100)
    expression  = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Calculation Method'
        verbose_name_plural = 'Calculation Methods'
        db_table = 'calculationMethod'

    def __str__(self):
        return self.name


class Plan(models.Model):
    STATUS = (

        ("branch","Go To nearest Branch"),
        ("online","Buy Online")
    )
    PAYTYPE = (
        ("postpaid","POSTPAID"),
        ("prepaid","PREPAID")
    )
    LINETYPE = (
        ("voice", "VOICE"),
        ("internet", "INTERNET")
    )
    country = models.ForeignKey(Country,null=True, on_delete=models.CASCADE,verbose_name='Country')

    operator_id = models.ForeignKey(operators, on_delete=models.CASCADE,verbose_name='operator')

    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=50,choices=STATUS,null=True,blank=True,verbose_name=_('e-commerce status'))
    website_description = models.TextField(max_length=1000, null=True, blank=True)
    commitment_months = models.IntegerField(null=True, blank=True,default=0)
    validity_days = models.IntegerField(null=True, blank=True,default=0)
    fee = models.IntegerField(null=True, blank=True,default=0)
    one_time_setup_fee = models.DecimalField(max_digits=10,decimal_places=2,null=True, blank=True,default=0)
    fee_notes = models.CharField(max_length=500, null=True, blank=True)
    initial_credit = models.IntegerField(null=True, blank=True,default=0)
    pay_type = models.CharField(max_length=50,choices=PAYTYPE,null=True,blank=True,verbose_name=_('pay type'))
    line_type = models.CharField(max_length=50,choices=LINETYPE,null=True,blank=True,verbose_name=_('line type'))
    plan_type = models.BooleanField(default=False,verbose_name="only sim")
    special_conditions = models.CharField(max_length=100, null=True, blank=True)
    subscription_fee = models.CharField(max_length=10, null=True, blank=True)
    monthly_fee = models.CharField(max_length=10, null=True, blank=True)
    is_upfront_payment = models.BooleanField(default=False)
    upfront_payment_per_year = models.IntegerField(null=True, blank=True)
    is_renewable = models.BooleanField(default=False)
    renewable_fee = models.CharField(max_length=10, null=True, blank=True)
    prorated = models.CharField(max_length=10, null=True, blank=True)
    validity = models.CharField(max_length=10, null=True, blank=True)
    vanity_number = models.CharField(max_length=10, null=True, blank=True)
    otp_method = models.CharField(choices=get_one_time_payment_method(), null=True, blank=True,
                                  verbose_name=_('One Time payment Calculation Method'), max_length=10,
                                  help_text=get_opt_help_text())
    mf_method = models.CharField(choices=monthly_fee_calculation_method(), null=True, blank=True,
                                 verbose_name=_('Monthly Fees Calculation Method'), max_length=10,
                                 help_text=get_mf_help_text())

    otp = models.CharField(choices=get_one_time_payment_method(), null=True, blank=True,
                           verbose_name=_('One Time payment Calculation Method'), max_length=10,
                           help_text=get_opt_help_text())
    mf = models.CharField(choices=monthly_fee_calculation_method(), null=True, blank=True,
                          verbose_name=_('Monthly Fees Calculation Method'), max_length=10,
                           help_text=get_mf_help_text())
    publication_date = models.DateTimeField(
        verbose_name=_('Activate Plan on:'),
        default=timezone.now)
    publication_date_end = models.DateTimeField(
        verbose_name=_('Deactivate Plan on:'),
        null=True,blank=True)
    plan_url_english = models.CharField(max_length=1000, null=True,
                                        verbose_name=_('Buy Online English URL'))
    plan_url_arabic = models.CharField(max_length=1000, null=True,
                                       verbose_name=_('Buy Online Arabic URL'))
    plan_url_english_near = models.CharField(max_length=1000, null=True,
                                             verbose_name=_('Nearest Store English URL'))
    plan_url_arabic_near= models.CharField(max_length=1000, null=True,
                                           verbose_name=_('Nearest Store Arabic URL'))

    objects = models.Manager()
    mobile_plan_objects = MobilePlanManager()
    mobile_internet_objects = MobileInternetManager()

    class Meta:
        verbose_name = 'plan'
        verbose_name_plural = 'plans'
        db_table = 'plan'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.line_type == "voice":
            return reverse('operatordetail', kwargs={'slug': self.slug})
        else:
            return "/mobile_internet/{slug}".format(slug=self.slug)

    @property
    def e_commerce_status(self):
        if self.status == 'online':
            return True
        if self.status == 'branch':
            return False
        return False

    @property
    def available_data(self):
        return get_available_data(self)

    @property
    def otp_value(self):
        return calculate_otp(self)

    @property
    def otp_value_only_sim(self):
        return calculate_otp(self, sim="sim")

    @property
    def mf_value(self):
        return calculate_mf(self)

    @property
    def mf_value_only_sim(self):
        return calculate_mf(self, sim="sim")


def plan_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(plan_pre_save_receiver, sender=Plan)


def plan_post_save_receiver(sender,instance,*args,**kwargs):

    if not hasattr(instance,'message'):
        m = Message(plan=instance)
        m.save()

    if not hasattr(instance,'data'):
        d = Data(plan=instance)
        d.save()

    if not hasattr(instance,'call'):
        c = Call(plan=instance)
        c.save()


post_save.connect(plan_post_save_receiver, sender=Plan)


class Message(models.Model):
    """
    Message table corresponds to SMS of plan 'SMS To all Networks free SMS','On Same Network free SMS',
    'To other Networks free SMS','Local free SMS' for donut calculation

    """
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE,related_name="message")

    sms_to_all_networks_free_sms = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('SMS To all Networks free SMS'))
    sms_to_all_networks_after_consumption = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('SMS To all Networks Rate/SMS after consumption (SAR)'))
    sms_to_all_networks_rate = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('SMS To all Networks Rate'))
    on_same_net_free_sms = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('On Same Network free SMS'))
    on_same_net_rate_sms_after_consumption = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('On Same Network Rate/SMS after consumption'))
    on_same_net_sms_rate = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('On the Same Network SMS rate'))
    to_other_networks_free_sms = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('To other Networks  free SMS'))
    to_other_net_rate_sms_after_consumption = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('To other Networks Rate/SMS after consumption'))
    to_other_networks_sms_rate = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('To other Networks SMS rate'))
    local_free_sms = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Local free SMS'))
    local_sms_rate = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Local SMS rate'))
    donut_message_val = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Donut Message Value'))

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        db_table = 'message'
    #
    # def __str__(self):
    #     return self.plan

    @property
    def available_data(self):
        return get_available_data(self)


def message_pre_save_receiver(sender,instance,*args,**kwargs):

    instance.donut_message_val = instance.sms_to_all_networks_free_sms + instance.on_same_net_free_sms \
                                 + instance.to_other_networks_free_sms + instance.local_free_sms


pre_save.connect(message_pre_save_receiver, sender=Message)


class Price(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    class Meta:
        verbose_name = 'price'
        verbose_name_plural = 'prices'
        db_table = 'planPrice'

    # def __str__(self):
    #     return self.plan


# class AppAccess(models.Model):
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
#     app_name = models.CharField(max_length=10, null=True, blank=True)
#
#     class Meta:
#         verbose_name = 'app_access'
#         verbose_name_plural = 'app_accesses'
#         db_table = 'app_access'
#         managed = False
#
#     def __str__(self):
#         return self.app_name


class Data(models.Model):
    """
    'Free Internet Quota (MB)','Additional free Internet Quota (GB)','Social Media Free MB'
    includes for donut calculation

    """
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE, related_name="data")
    free_internet = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Free Internet Quota (MB)'))
    add_free_internet = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Additional free Internet Quota (MB)'))
    free_internet_wifi = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Free Internet Wi-Fi (MB)'))
    fair_policy = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Fair policy (Daily MB)'))
    after_quota_fair_policy = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('After /quota Fair policy consumption(kbps)'))
    rate_after_consumption = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Rate/MB after consumption(SAR)'))
    data_usage_rate = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Data Usage Rate/MB'))
    free_access_to_apps = models.BooleanField(
        default=False, verbose_name=_('Free Access to Apps (Yes/No)'))
    social_media_free_mb = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Social Media Free MB'))
    Social_includes = MultiSelectField(choices=get_available_apps(),null=True,blank=True)
    donut_data_val = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Donut Data Value'))

    class Meta:
        verbose_name = 'data'
        verbose_name_plural = 'datas'
        db_table = 'data'

    @property
    def available_data(self):
        return get_available_data(self)


def data_pre_save_receiver(sender,instance,*args,**kwargs):

    instance.donut_data_val = instance.free_internet + instance.add_free_internet + instance.social_media_free_mb


pre_save.connect(data_pre_save_receiver, sender=Data)


class Call(models.Model):
    """
    plan table 'Calls to same package Free minutes','Calls to All networks Free minutes','On Same Network free minutes'
    'To Other Networks free minutes','Land line free minutes','Local free minutes' are used for donut calculation should
    be an integer field
    """
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE, related_name="call")
    calls_to_same_package_free_minutes = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Calls to same package free minutes '))
    calls_to_all_network_free_minutes = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Calls to All networks free minutes '))
    calls_to_all_network_rate_min_after_cons = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('Calls to All network rate/min after consumption'))
    calls_to_all_network_rate_min = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('Calls to All network rate/min'))
    on_same_net_free_minutes = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('On Same Network free minutes'))
    on_same_net_rate_minutes = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('On Same Network Rate/min after consumption'))
    on_same_net_voice_call_rate = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('On Same Network voice call rate'))
    on_same_net_voice_call_rate_peak_hour = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('On Same Network voice call rate (Peak Hours)'))
    on_same_net_voice_call_rate_off_peak_hour = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('On Same Network voice call rate (Off-Peak Hours)'))
    to_other_network_free_minutes = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('To Other Networks free minutes'))
    to_other_network_voice_call_rate_min_after_cons = models.CharField(
        max_length=10, null=True, blank=True,verbose_name=_('To Other Networks voice callrate/min after consumption '))
    to_other_network_voice_call_rate_min = models.CharField(
        max_length=10, null=True, blank=True,
        verbose_name=_('To Other Networks voice call rate/min'))
    to_other_network_voice_call_rate_peak_hour = models.CharField(
        max_length=10, null=True, blank=True,
        verbose_name=_('To Other Networks voice call rate (Peak Hours)'))
    to_other_network_voice_call_rate_off_peak_hour = models.CharField(
        max_length=10, null=True, blank=True,
        verbose_name=_('To Other Networks voice call rate (Off-Peak Hours)'))
    land_line_free_minutes = models.IntegerField(
        default=0, null=True, blank=True,
        verbose_name=_('Land line free minutes'))
    land_line_voice_call_rate_peak_hours = models.CharField(
        max_length=10, null=True, blank=True,
        verbose_name=_('Land line voice call rate (Peak Hours)'))
    land_line_voice_call_rate_off_peak_hours = models.CharField(
        max_length=10, null=True, blank=True,
        verbose_name=_('Land line voice call rate (Off-Peak Hours)'))
    local_free_minutes = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Local free minutes'))
    local_voice_call_rate_peak_hour = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('Local voice call rate (Peak Hours)'))
    local_voice_call_rate_off_peak_hour = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('Local voice call rate (Off-Peak Hours)'))
    donut_call_val = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Donut call Value'))

    class Meta:
        verbose_name = 'call'
        verbose_name_plural = 'calls'
        db_table = 'call'

    # def __str__(self):
    #     return self.plan
    @property
    def available_data(self):
        return get_available_data(self)


def call_pre_save_receiver(sender,instance,*args,**kwargs):

    instance.donut_call_val = instance.calls_to_same_package_free_minutes + instance.calls_to_all_network_free_minutes\
                              + instance.on_same_net_free_minutes + instance.to_other_network_free_minutes + \
                              instance.land_line_free_minutes + instance.local_free_minutes


pre_save.connect(call_pre_save_receiver, sender=Call)


class MMS(models.Model):
    """
    Arabic translation 'off_net_mms'

    """
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE, related_name="mms")
    on_net_mms = models.CharField(
        max_length=10, null=True, blank=True,
        verbose_name=_('On-net MMS Rate'))
    off_net_mms = models.CharField(
        max_length=10, null=True, blank=True,
        verbose_name=_('off-net MMS Rate'))
    international_mms_rate = models.CharField(
        max_length=10, null=True, blank=True,
        verbose_name=_('International MMS Rate'))

    class Meta:
        verbose_name = 'MMS'
        verbose_name_plural = 'MMS'
        db_table = 'MMS'

    # def __str__(self):
    #     return self.plan

    @property
    def available_data(self):
        return get_available_data(self)


class Bundle(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    bundle_name = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'bundle'
        verbose_name_plural = 'bundles'
        db_table = 'bundle'

    def __str__(self):
        return self.bundle_name


class BundleAttributes(models.Model):
    bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=20, null=True, blank=True)
    attribute_value = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'bundle attribute'
        verbose_name_plural = 'bundle attributes'
        db_table = 'bundleAttribute'

    def __str__(self):
        return self.bundle


class InternationalBenefit(models.Model):

    """
    Arabic translation to be included
    'International Roaming Benefits','International Rates promotion','International Minute Rate'

    """
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE, related_name="international_benefit")
    international_free_minutes = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('International free minutes'))
    international_roaming_benefit = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('International Roaming Benefits'))
    international_roaming_countries = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('Internet roaming countries'))
    international_free_sms = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('International free SMS'))
    international_sms_rate = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_('International SMS rate'))
    roaming_free_data = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Roaming Free Data Quota (MB)'))
    international_rate_promotions = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('International Rates promotion'))
    international_minute_rate = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('International Minute Rate'))

    flexible_free_minutes = models.IntegerField(
        default=0, null=True, blank=True, verbose_name=_('Flexible free minutes (Local or International)'))

    class Meta:
        verbose_name = 'International Benefit'
        verbose_name_plural = 'International Benefits'
        db_table = 'internationalBenefits'

    @property
    def available_data(self):
        return get_available_data(self)


class AdditionalBenefit(models.Model):
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE, related_name="additional_benefit")
    monthly_bundle_credit = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Monthly bundle Credit'))
    special_number_benefits = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Special Number Benefits'))
    welcome_package_benefits = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('welcome package Benefits'))
    contract_renewal_benefits = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Contract Renewal Benefits'))
    benefits = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Benefits'))
    device_discount_benefits = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Device discount Benefit'))
    other_benefits = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Other benefits'))
    eligibility = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Eligibility'))

    class Meta:
        verbose_name = 'Additional Benefit'
        verbose_name_plural = 'Additional Benefits'
        db_table = 'additionalBenefit'

    @property
    def available_data(self):
        return get_available_data(self)


class Subscription(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="subscription_method")
    subscription_method = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('subscription method'))
    cancellation_method = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Cancellation method'))

    class Meta:
        verbose_name = 'Subscription method'
        verbose_name_plural = 'Subscription methods'
        db_table = 'subscriptionMethod'

    @property
    def available_data(self):
        return get_available_data(self)


class PlanAdditionalAttribute(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="plan_add_attr")
    attr_name = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Attribute Name'))
    attr_value = models.CharField(
        max_length=500, null=True, blank=True, verbose_name=_('Attribute Value'))

    class Meta:
        verbose_name = 'Plan Additional Attribute'
        verbose_name_plural = 'Plan Additional Attributes'
        db_table = 'planaddattr'


# class PlanManaged(Plan):
#
#     class Meta:
#         proxy = True


class BulkUpload(models.Model):
    otp_method = models.CharField(choices=get_one_time_payment_method(), null=True, blank=True,
                                  verbose_name=_('One Time payment Calculation Method'), max_length=10,
                                  help_text=get_opt_help_text())
    mf_method = models.CharField(choices=monthly_fee_calculation_method(), null=True, blank=True,
                                 verbose_name=_('Monthly Fees Calculation Method'), max_length=10,
                                 help_text=get_mf_help_text())

    plans = models.ManyToManyField(blank=True, related_name='bulkupload', to=Plan, verbose_name="Plans")

    class Meta:
        verbose_name = 'Bulk plan upload'
        verbose_name_plural = 'Bulk plan uploads'
        db_table = 'bulkupload'


class DeviceInstallment(models.Model):
    LINETYPE = (
        ("voice", "VOICE"),
        ("internet", "INTERNET")
    )
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True)
    operator= models.ForeignKey(operators, on_delete=models.CASCADE, verbose_name='Operators',null=True)
    line_type = models.CharField(max_length=50, choices=LINETYPE, null=True, blank=True, verbose_name=_('Line Type'))
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="device_installment_plan",null=True,
                             blank=True,)
    phone = models.ForeignKey(DeviceRam, on_delete=models.CASCADE, related_name="device_installment_phone",
                               null=True, blank=True,)
    plan_device = models.ManyToManyField(blank=True, related_name='device_installment_device', to=PlanDevice,
                                         verbose_name="Plan Device")
    discount = models.IntegerField(null=True, blank=True, verbose_name="Discount in %")
    installment_value = models.IntegerField(null=True, blank=True, verbose_name="Installment Value",default=0)
    device_upfront_otp = models.IntegerField(null=True, blank=True, verbose_name="Device Upfront One Time Payment",default=0)
    commitment_months = models.IntegerField(null=True, blank=True, default=0,
                                            verbose_name="Commitment Months/Contract Period")
    otp_method = models.CharField(choices=get_one_time_payment_method(), null=True, blank=True,
                                  verbose_name=_('One Time payment Calculation Method'), max_length=10,
                                  help_text=get_opt_help_text())
    mf_method = models.CharField(choices=monthly_fee_calculation_method(), null=True, blank=True,
                                 verbose_name=_('Monthly Fees Calculation Method'), max_length=10,
                                 help_text=get_mf_help_text())

    device_url_english = models.CharField(max_length=1000, null=True, blank=True,
                                        verbose_name=_('Buy Online English URL'))
    device_url_arabic = models.CharField(max_length=1000, null=True, blank=True,
                                       verbose_name=_('Buy Online Arabic URL'))
    device_url_english_near = models.CharField(max_length=1000, null=True, blank=True,
                                             verbose_name=_('Nearest Store English URL'))
    device_url_arabic_near = models.CharField(max_length=1000, null=True, blank=True,
                                            verbose_name=_('Nearest Store Arabic URL'))



    # def validate_unique(self, *args, **kwargs):
    #     super(DeviceInstallment, self).validate_unique(*args, **kwargs)
    #     try :
    #         obj = self.__class__.objects. \
    #             filter(plan=self.plan,country=self.country).get(phone=self.phone)
    #     except ObjectDoesNotExist:
    #         pass
    #
    #
    #
    #
    #
    #         raise ValidationError(
    #             message='Plan can be configured to one phone only for a country',
    #             code='unique_together',
    #         )

    class Meta:
        verbose_name = 'Device Instalment Configuration'
        verbose_name_plural = 'Device Instalment Configurations'






