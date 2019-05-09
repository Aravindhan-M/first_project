from django.db.models import Manager
from django.utils import timezone
from django.db.models import Q
# from django.db.models import QuerySet


# class AdQuerySet(QuerySet):
#     def add_density(self):
#         return self.annotate(
#             count= self.device_installment_plan.filter(plan__id=1)
#         )


class MobilePlanManager(Manager):

    def get_queryset(self):

        return super(MobilePlanManager, self).get_queryset().filter(Q(publication_date__lte=timezone.now()),
                                                                    Q(publication_date_end__gt=timezone.now()) |
                                                                    Q(publication_date_end__isnull=True),
                                                                    Q(is_active=True),
                                                                    Q(line_type__exact='voice'))


class MobileInternetManager(Manager):
    def get_queryset(self):
        return super(MobileInternetManager, self).get_queryset().filter(Q(publication_date__lte=timezone.now()),
                                                                    Q(publication_date_end__gt=timezone.now()) |
                                                                    Q(publication_date_end__isnull=True),
                                                                    Q(is_active=True),
                                                                    Q(line_type__exact='internet'))