from django.core.management.base import BaseCommand
from phone.models import Phone


class Command(BaseCommand):
    help = 'Update for testing'

    def handle(self, *args, **kwargs):

        try:
            print("testing command")
            object_list = Phone.objects.all()
            for c, obj in enumerate(object_list):
                var = (" ".join(obj.name.split(" ")[:3])).replace(",", "").replace("-", "").replace("(", "")\
                    .replace(")", "").strip()
                obj.title_tst = var
                obj.save()
                print(var, " saved")
                print(c+1, " obj saved")

        except Exception as e:
            print(e, "Exception occurred")
