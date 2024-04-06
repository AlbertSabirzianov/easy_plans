from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, View
from . import forms


class MainPage(TemplateView):
    template_name = 'users/main_page.html'


class UserCreateView(CreateView):
    form_class = forms.SignUpForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:main')


class UserLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('users:main')

    def get_success_url(self):
        return self.success_url


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('users:main')
