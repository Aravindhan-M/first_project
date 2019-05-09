
from django.views.generic.list import ListView
from django.views.generic import DetailView
from phone.models import Phone








class PhoneMobileView(ListView):
    model = Phone
    paginate_by = 20
    context_object_name = 'phones'
    template_name = 'test.html'

    def get_queryset(self):
        request = self.request

        return Phone.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['next'] = self.request.META.get('HTTP_REFERER')
        context['count'] = self.get_queryset().count()
        context['categories'] = ['Mobiles']
        context['stores'] = ['Lulu']
        # context['colors'] = self.get_queryset().values_list("color",flat=True).distinct()
        #context['internals'] = refine_internal(list(self.get_queryset().values_list("internal",flat=True).distinct()))
        return context


