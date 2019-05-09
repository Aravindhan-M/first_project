

from django.urls import path
from .views import MobilePlanView,MobilePlanHome

urlpatterns = [

    path('', MobilePlanHome.as_view(), name='mobileplans'),
    path('<slug:slug>', MobilePlanView.as_view(),name="mobile" ),


]
