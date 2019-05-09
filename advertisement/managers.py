import random

from advertisement.querysets import AdQuerySet
from django.db.models import Manager, Count


class AdManager(Manager):
    def get_queryset(self):
        return AdQuerySet(self.model)

    def public(self):
        return self.get_queryset().public()

    def zone_ads(self, zone,page):
        return self.get_queryset().zone_ads(zone,page)

    def random_ad(self, zone,page):
        ads = []
        for ad in self.zone_ads(zone,page).public():
            ads += [ad] * ad.weight
        if not ads:
            return None
        return random.choice(ads)
