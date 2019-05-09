from phone.views import Phone
from django.views.generic import DetailView,TemplateView
from plan.forms import PlanForm

class MobilePlanView(DetailView):
    model = Phone
    context_object_name = 'detail'
    template_name = 'plan_baker_inner_page01.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MobilePlanHome(TemplateView):
    template_name = 'plan_baker_inner_page01.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_class'] = PlanForm()
        return context
