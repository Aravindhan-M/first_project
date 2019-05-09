"""planbaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

admin.site.site_header = "Plan Baker Admin"
admin.site.site_title = "Plan Baker Admin Portal"
admin.site.index_title = "Welcome to Plan Baker Admin Portal"
urlpatterns = [





]
urlpatterns += i18n_patterns(

    #path('', TemplateView.as_view(template_name="home.html"),name='home'),
    path('', include('homepage.urls')),
    path('search/',include('search.urls')),
    #path('phone/',include('phone.url'),name='phone'),
    path('phones/', include('phone.urls')),
    path('ads/', include('advertisement.urls')),
    path('registration/', include('user.urls')),
    path('register/', TemplateView.as_view(template_name="register_login.html"), name='sign_up_in'),
    path('mobile_internet/', include('mobile_internet.urls')),
    path('fixed_internet/', include('fixed_internet.urls')),

    path('buyphones/', TemplateView.as_view(template_name="planbaker_04.html"),name='buyphones'),
    path('operators/', include('plan.urls')),
    #path('operators/', TemplateView.as_view(template_name="Planbaker_03.html"), name='operators'),
    #path('viewoperators/', TemplateView.as_view(template_name="viewoperator.html"), name='viewoperators'),
    path('mobileplans/', include('plan.urls')),

    path('adsl/', TemplateView.as_view(template_name="planbaker_05.html"),name='adsl'),
    path('add/', TemplateView.as_view(template_name="404.html"),name='add'),
    path('admin/', admin.site.urls),
    path('survey/', include('survey.urls')),
    path('test/',include('pages.urls')),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
