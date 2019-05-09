from django.urls import path
from .views import *


urlpatterns = [

   path('', MobilePlanHome.as_view(), name='mobileplans'),
   path('operators/', PlanView.as_view(),name='operators'),
   path('ajax/', ajax_result, name='plan_ajax'),
   path('ajax-list/', PlanPhoneList.as_view(), name='plan_ajax_list'),
   path('plan-count/', plan_count, name='plan_count'),
   path('mobile_plan_count/', mobile_internet_count, name='mobile_plan_count'),
   # path('<str:phone_slug>/<str:phone_name>/<str:phone_media>/', PlanView.as_view(), name='operator-mob'),
   # path('', PlanView.as_view(), name='operators_phone'),
   path('device/<pk>/', DeviceDetailView.as_view(), name='devicedetailpk'),
   path('device/<pk>/<param>/', DeviceDetailView.as_view(), name='devicedetail'),
   path('operators/<slug:slug>/', PlanDetailView.as_view(), name='operatordetail'),
   path('ajax-plan-admin/', query_operator_country, name='operator_country'),
   path('ajax-plan-country-admin/',query_plan_country,name='plan_country_admin'),
   path('ajax-plan-country-phone-admin/', query_phone_plan_country, name='plan_phone_country_admin'),
   path('ajax-device-installment-admin/', query_device_installment, name='plan_device_installment_admin')

]
