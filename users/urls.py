from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegistrationView, UserLoginView, logout


app_name = 'users'


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
