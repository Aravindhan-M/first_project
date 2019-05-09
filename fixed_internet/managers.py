from django.db.models import Manager


class FixedInternetManager(Manager):

    def get_queryset(self):
        return super(FixedInternetManager, self).get_queryset().filter(
                                                                    is_active=True,
                                                                    )