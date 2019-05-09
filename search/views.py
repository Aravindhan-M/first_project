from phone.utils import refine_internal
from django.views.generic.list import ListView
from el_pagination.views import AjaxListView
from homepage.utils import get_context_obj
from phone.models import Phone
from phone.forms import PhoneSearchForm
import re


# class SearchPhoneView(ListView):
#     paginate_by = 5
#     context_object_name = 'phones'
#     template_name = 'phone/phone_home.html'
#
#
#     def get_queryset(self):
#         request = self.request
#
#         method_dict = request.GET
#
#         query = method_dict.get('q',None)
#
#         print(query,"qqqq")
#         print(type(query), "qqqq")
#
#         if query is None:
#             return Phone.objects.all()
#         else:
#             return Phone.objects.filter(name__search=query)
#
#     def hasNumbers(self,inputString):
#         return bool(re.search(r'\d', inputString))
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         con = get_context_obj(self.request)
#         context['obj'] = con['obj']
#         context['country'] = con['country']
#         context['user'] = self.request.user
#         context['next'] = self.request.META.get('HTTP_REFERER')
#         context['count'] = self.get_queryset().count()
#         context['lucount'] = self.get_queryset().filter(product_url__icontains='www.luluhypermarket.com').count()
#         context['socount'] = self.get_queryset().filter(product_url__icontains='https://saudi.souq.com').count()
#         context['categories'] = ['Mobiles']
#         context['stores'] = ['Lulu','Souq']
#         #context['colors'] = [i for i in Phone.objects.values_list("color",flat=True).distinct() if i is not None and not self.hasNumbers(i)]
#         context['internals'] = refine_internal(list(Phone.objects.values_list("internal",flat=True).distinct()))
#         return context


class SearchPhoneView(AjaxListView):
    context_object_name = 'phones'
    template_name = 'phone/phone_home.html'
    page_template = 'phone/phone_home_list.html'
    model = Phone

    def __init__(self):
        self.form_class = None

        super(SearchPhoneView, self).__init__()

    def get_queryset(self):
        qs =Phone.objects.all()
        request = self.request

        method_dict = request.GET

        query = method_dict.get('q',None)
        store = method_dict.get('store_div_id_store',None)
        color = method_dict.get('color_div_id_color',None)
        memory = method_dict.get('memory_div_id_memory',None)
        price = method_dict.get('price', None)
        sort_by = method_dict.get('sort_by', None)
        print(price,"priceee")

        if query:
            qs = qs.filter(name__search=query)
        if store:
            qs = qs.filter(stores__store=store)
        if color:
            qs = qs.filter(colors__color=color)
        if memory:
            qs = qs.filter(rams__ram=memory)
        if price:
            prices = price.split("to")
            qs = qs.filter(price__gte=prices[0],price__lte=prices[1])
        if sort_by:
            qs = qs.order_by(sort_by)

        self.form_class = PhoneSearchForm(qs = qs,request=self.request)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        con = get_context_obj(self.request)
        context['form_class'] = self.form_class
        context['obj'] = con['obj']
        context['country'] = con['country']
        context['user'] = self.request.user
        context['next'] = self.request.META.get('HTTP_REFERER')

        context['categories'] = ['Mobiles']

        return context




