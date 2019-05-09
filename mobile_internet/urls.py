from django.urls import path
from .views import MoboileInternetHome , MobileInternetList, MobileInternetDetail, internet_devices

urlpatterns = [

     path('', MoboileInternetHome.as_view(), name='mobileinternet'),
     path('mobile_internet_list',MobileInternetList.as_view(), name='mobile_internet_operators'),
     path('<slug:slug>/', MobileInternetDetail.as_view(), name='mobile_internet_detail' ),
     path('devices', internet_devices, name='internet_devices'),
]