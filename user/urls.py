from django.urls import path
from . import views


urlpatterns = [
    path('', views.RegisterLoginView.as_view(), name='registration'),
    path('login', views.RegisterLoginView.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    # path('', views.registration, name='registration'),
    path('sendotp/', views.handle_opt, name='otp-verification'),
    # path('registration', views.registration, name='registration'),
    # path('ad', views.ad, name='adpage'),
    # path('verification/', views.phone_verification, name='phone_verification'),
    # path('verification/token/', views.token_validation, name='token_validation'),
    # path('verified/', views.verified, name='verified'),
]