from django.urls import path
from .views import *


urlpatterns = [

   path('', home_page, name='home'),
   path('set_session/', update_session, name='set-session'),
   path('set_currency/', update_currency, name='set-currency'),


]
