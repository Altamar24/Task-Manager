from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import CreateUser, UserLoginForm

User = get_user_model()


class RegistrationView(CreateView):
    """Класс RegistrationView позволяет зарегестрироваться пользователю"""

    model = User
    form_class = CreateUser
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')


class UserLoginView(LoginView):
    """Класс UserLoginView позволяет войти пользователю по логину и паролю"""

    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('')


def logout(request):
    """Метод logout позволяет пользователю выйти из системы"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))
