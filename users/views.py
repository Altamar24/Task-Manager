from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import CreateUser, UserLoginForm

User = get_user_model()


class RegistrationView(CreateView):
    model = User
    form_class = CreateUser
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
