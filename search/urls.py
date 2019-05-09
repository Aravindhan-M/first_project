from django.urls import path
from .views import SearchPhoneView

urlpatterns = [

    path('', SearchPhoneView.as_view(), name='search'),


]
