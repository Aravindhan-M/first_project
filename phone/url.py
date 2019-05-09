from django.urls import path
from .views import PhoneMobileView

urlpatterns = [


   path('', PhoneMobileView.as_view(), name='phone-mobile'),


]
