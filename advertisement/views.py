
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from advertisement.conf import settings
from advertisement.models import Ad, Impression , Click
from django.shortcuts import render
from django.http import JsonResponse
from advertisement.utils import get_client_ip,get_random_images,get_random_videos


class AdClickView(
        SingleObjectMixin, View):

    def get_queryset(self):
        return Ad.objects.all()

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        if request.session.session_key:
            click, created = Click.objects.get_or_create(
                ad=ad,
                session_id=request.session.session_key,
                defaults={
                    'click_date': timezone.now(),
                    'source_ip': get_client_ip(request),
                })

        return HttpResponseRedirect(ad.url)

def index(request):
    return render(request, 'ad.html')


def render_ads_zone(request):
    zone = request.GET.get('zone', None)
    page = request.GET.get('page', None)
    context = None
    try:
        ad = Ad.objects.random_ad(zone,page)

        if ad is not None:
            if request.session.session_key:
                impression, created = Impression.objects.get_or_create(
                    ad=ad,
                    session_id=request.session.session_key,
                    defaults={
                        'impression_date': timezone.now(),
                        'source_ip': get_client_ip(request),
                    })


        context={
            'title': ad.title,
            'ad_url' : ad.get_absolute_url(),
            'zone': settings.ADS_ZONES.get(zone, None),

            'image-device' : "random"
        }

        if ad.images.all():
            context['image_url']= get_random_images(ad.images.all())
        if ad.videos.all():
            context['video_url'] = get_random_videos(ad.videos.all())

    except Exception:
        pass
    return JsonResponse(context,safe=False)
