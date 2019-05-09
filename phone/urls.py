from django.urls import path
from .views import PhoneView,PhoneMobileView,PhoneViewAjax,MobileView,ajaxresult,PhoneHomePage,query_currency_country

urlpatterns = [


   path('', PhoneHomePage.as_view(),name="mobile"),
   path('ajax', ajaxresult, name="ajax-view"),
path('<slug:slug>', MobileView.as_view(), name="mobile-view"),
path('ajax-test', PhoneViewAjax.as_view(), name="ajax-test"),
path('ajax-currency/', query_currency_country, name="ajax-currency"),


]
