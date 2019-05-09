import random
from django.utils.translation import gettext_lazy
from django.conf import settings
dictionary = {
    "plan" : "MOBILE INTERNET",
    "mobileplans" : "MOBILE PLANS",
    "phones" : "MOBILE PHONES",
    "adsl" : "FIXED INTERNET",
    "register" : "REGISTER",
    "operators": "OPERATORS"
}

def get_zones_choices():
    for key in sorted(settings.ADS_ZONES):
        yield (key, gettext_lazy(settings.ADS_ZONES[key].get('name', 'Undefined')))


def get_pages_choices():
    for key in sorted(settings.ADS_PAGES):
        yield (key,dictionary[key])


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    print(x_forwarded_for)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', '')
    print(request.META.get('HTTP_X_REAL_IP', 'not'))
    return ip


def get_random_images(images):
    image_url = None
    try:
        img = random.choice(images)
        image_url = img.image.url
    except Exception:
        pass
    return image_url


def get_random_videos(videos):
    video_url = None
    try:
        video = random.choice(videos)
        video_url = video.video.url
    except Exception:
        pass
    return video_url

