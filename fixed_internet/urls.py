from django.urls import path
from .views import FixedInternetHome, FixedInternetList, FixedInternetDetail, fixed_count
urlpatterns=[
    path('', FixedInternetHome.as_view(), name='fixedinternet'),
    path('fixed_internet_list', FixedInternetList.as_view(), name='fixed_internet_operators'),
    path('fixed_count/', fixed_count, name='fixed_count'),
    path('<slug:slug>/', FixedInternetDetail.as_view(), name='fixed_internet_detail' ),

]