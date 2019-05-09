from django.db.models import Manager


class CountryManager(Manager):

    def get_queryset(self):
        return super(CountryManager, self).get_queryset().filter(is_active=True)

