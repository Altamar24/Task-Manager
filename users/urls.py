from django.contrib.auth import views as auth_views
from django.urls import path

from .views import RegistrationView, UserLoginView, logout


app_name = 'users'


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]
