from django.urls import path
from advertisement.views import AdClickView
from django.conf.urls import url
from . import views
app_name = 'advertisement'
urlpatterns = [

    path('', views.index, name='advertisement-request'),
    path('adreq/', views.render_ads_zone, name='advertisement-index'),
    url(r'^(?P<pk>\d+)/$', AdClickView.as_view(), name='ad-click'),

]







