from multiselectfield import MultiSelectField

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from .utils import unique_slug_generator,get_available_languages,get_available_currency
from .managers import CountryManager


class Country(models.Model):
    name = models.CharField(max_length=100,verbose_name="Short Name")
    slug = models.SlugField(max_length=60, null=True, blank=True)
    country_code = models.CharField(max_length=5,null = True,blank=True,verbose_name="Country Code")
    currency =MultiSelectField(choices=get_available_currency(),null=True,blank=True)
    default_currency = models.CharField(choices=get_available_currency(),null=True,
                                        verbose_name="Default Currency",max_length=20)
    allowed_laguages = MultiSelectField(choices=get_available_languages(),null=True,blank=True)
    country_full_name = models.CharField(max_length=100,null=True, blank=True,verbose_name="Full Name")
    country_flag = models.ImageField(verbose_name='Country Flag Image', max_length=255,null=True)
    country_banner = models.ImageField(verbose_name='Country Banner Image', max_length=255,null=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active_country = CountryManager()


    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'
        db_table = 'country'

    def __str__(self):
        return self.name


def country_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(country_pre_save_receiver, sender=Country)


class Phone(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=2050,null=True,blank=True)
    slug = models.SlugField(max_length=2050,null=True,blank=True)
    title = models.CharField(max_length=2000,null=True,blank=True)

    #color = models.CharField(max_length=100, null=True, blank=True)
    internal = models.CharField(max_length=100,null=True,blank=True)
    external = models.CharField(max_length=100, null=True, blank=True)
    #ram = models.CharField(max_length=100, null=True, blank=True)
    processor = models.CharField(max_length=100, null=True, blank=True)
    sim = models.CharField(max_length=100, null=True, blank=True)
    sim_slot = models.CharField(max_length=100, null=True, blank=True)
    os= models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=100, null=True, blank=True)
    other_features = models.TextField(max_length=700,null=True,blank=True)
    size = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    display_type = models.CharField(max_length=75,null=True,blank=True)
    resolution = models.CharField(max_length=75,null=True,blank=True)
    primary_camera = models.CharField(max_length=75,null=True,blank=True)
    secondary_camera = models.CharField(max_length=75,null=True,blank=True)
    video_recording = models.CharField(max_length=75,null=True,blank=True)
    flash = models.CharField(max_length=75,null=True,blank=True)
    network = models.CharField(max_length=100,null=True,blank=True)
    wifi = models.CharField(max_length=100, null=True, blank=True)
    bluetooth = models.CharField(max_length=100, null=True, blank=True)
    nfc = models.CharField(max_length=100, null=True, blank=True)
    port = models.CharField(max_length=100,null=True,blank=True)
    #brand = models.CharField(max_length=51, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    title_tst = models.CharField(max_length=1000, null=True, blank=True)
    model = models.CharField(max_length=70, null=True, blank=True)
    price_notes = models.CharField(max_length=100,null=True,blank=True)
    currency_code = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=3000,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    last_modified_date = models.DateTimeField(auto_now=True,blank=True, null=True)

    product_url = models.URLField(max_length=2000,blank=True, null=True)

    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'
        db_table = 'phone'

    def __str__(self):
        return self.name


def phone_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(phone_pre_save_receiver, sender=Phone)


def create_scrapped_phone(sender, instance, created, **kwargs):
    content_type = ContentType.objects.get_for_model(instance)
    try:
        phone_content = PhoneContent.objects.get(content_type=content_type,
                              object_id=instance.id)
    except PhoneContent.DoesNotExist:
        phone_content = PhoneContent(content_type=content_type, object_id=instance.id)

    phone_content.save()


post_save.connect(create_scrapped_phone, sender=Phone)


class PhoneAttribute(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    color = models.CharField(max_length=5, null=True, blank=True)
    ram = models.CharField(max_length=10, null=True, blank=True)
    max_memory_card_size = models.CharField(max_length=10, null=True, blank=True)
    max_memory_card = models.IntegerField(null=True, blank=True)
    music_playback_time = models.CharField(max_length=10, null=True, blank=True)
    video_playback_time = models.CharField(max_length=10, null=True, blank=True)
    standby_talk_time = models.CharField(max_length=10, null=True, blank=True)
    display_size = models.CharField(max_length=10, null=True, blank=True)
    display_color = models.CharField(max_length=10, null=True, blank=True)
    resolution = models.CharField(max_length=10, null=True, blank=True)
    pixel_density = models.CharField(max_length=10, null=True, blank=True)
    generation = models.CharField(max_length=10, null=True, blank=True)
    bluetooth = models.CharField(max_length=100, null=True, blank=True)
    wifi_features = models.CharField(max_length=150, null=True, blank=True)
    volte = models.CharField(max_length=10, null=True, blank=True)
    usb_connectivity = models.CharField(max_length=10, null=True, blank=True)
    sim_slot = models.IntegerField(null=True, blank=True)
    sim_size = models.CharField(max_length=10, null=True, blank=True)
    tracking_system  = models.CharField(max_length=10, null=True, blank=True)
    processor = models.CharField(max_length=50, null=True, blank=True)


    class Meta:
        verbose_name = 'phone attribute'
        verbose_name_plural = 'phone attributes'
        db_table = 'phoneAttribute'

    # def __str__(self):
    #     return self.phone


class AdditionPhoneAttribute(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=150,null=True, blank=True)
    attribute_value = models.CharField(max_length=150,null=True, blank=True)

    class Meta:
        verbose_name = 'additional attribute'
        verbose_name_plural = 'additional attributes'
        db_table = 'scrape_additional_attribute'

    def __str__(self):
        return self.phone.name


class Brand(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='brands')
    name = models.CharField(max_length=40,null=True, blank=True)
    description = models.CharField(max_length=200,blank=True,null=True)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
        db_table = 'brand'

    def __str__(self):
        return self.name


class Store(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='stores')
    store = models.CharField(max_length=40,null=True, blank=True)

    class Meta:
        verbose_name = 'store'
        verbose_name_plural = 'stores'
        db_table = 'store'


class Color(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='colors')
    color = models.CharField(max_length=40,null=True, blank=True)

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'
        db_table = 'color'


    # def __str__(self):
    #     return self.name


# class Price(models.Model):
#     website = models.ForeignKey(Website, on_delete=models.CASCADE)
#     phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
#     price = models.DecimalField(decimal_places=2,max_digits=7)
#
#     class Meta:
#         verbose_name = 'price'
#         verbose_name_plural = 'prices'
#         db_table = 'price'
#
#
#     def __str__(self):
#         return self.website + ":" + self.phone + ":" + self.price


class RAM(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='rams')
    ram = models.CharField(max_length=40,blank=True,null=True)

    class Meta:
        verbose_name = 'ram'
        verbose_name_plural = 'ram'
        db_table = 'ram'


    # def __str__(self):
    #     return self.phone + ":" + self.memory


class Image(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='images')
    path = models.CharField(max_length=100,null=True, blank=True)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
        db_table = 'image'


    # def __str__(self):
    #     return self.phone + ":" + self.path


class Thumbnail(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    path = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'thumbnail'
        verbose_name_plural = 'thumbnails'
        db_table = 'thumbnail'

    def __str__(self):
        return self.image


class PhoneContent(models.Model):
    """
    This model will record post save of both plan phone and scrapped phone, in case of scrapping we need to update
    manually from query, the reason for this is we need to show both scrapped and plan phone in mobilephones model
    planbaker=# select * from phone_phonecontent;
 id | object_id | content_type_id
----+-----------+-----------------
    """
    """
    PhoneContent.objects.all().order_by('-content_type_id')
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    @property
    def phone_type(self):

        return isinstance(self.content_object,Phone)

    def __str__(self):
        return "{0}".format(self.content_object.name,
                                  )

