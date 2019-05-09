# from django.db.models import QuerySet
# from django.utils import timezone
#
#
# class MobilePlanQuerySet(QuerySet):
#
#     def all(self):
#
#         return self.filter(
#             publication_date__lte=timezone.now(),
#             publication_date_end__gt=timezone.now(),
#             is_active = True,
#             line_type__exact = 'voice'
#         )
