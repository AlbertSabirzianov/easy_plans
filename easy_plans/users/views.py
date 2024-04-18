import json

from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView, View, UpdateView, ListView, DeleteView
from . import forms
from .models import WorkPlace


class MainPage(TemplateView):
    template_name = 'users/main_page.html'


class UserCreateView(CreateView):
    form_class = forms.SignUpForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:main')


@method_decorator(csrf_exempt, name='dispatch')
class SignatureUploadView(View, LoginRequiredMixin):

    def post(self, request):
        request.user.signature = json.loads(request.body).get('drawing')
        request.user.save()
        return HttpResponse('OK')


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


class PersonalPageUpdateView(UpdateView, LoginRequiredMixin):
    model = get_user_model()
    fields = ('first_name', 'last_name', "father_name")
    template_name = 'users/update_person.html'
    success_url = reverse_lazy('users:update_person')

    def get_object(self, queryset=None):
        return self.request.user


class WorkPlacesView(LoginRequiredMixin, ListView):
    model = WorkPlace
    template_name = 'users/works.html'

    def get_queryset(self):
        return WorkPlace.objects.filter(user=self.request.user)


class WorkPlacesAdd(LoginRequiredMixin, CreateView):
    model = WorkPlace
    form_class = forms.WorkAddForm
    template_name = 'users/add_work.html'
    success_url = reverse_lazy('users:works')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save(request=self.request)
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class DeleteWorkPlace(LoginRequiredMixin, DeleteView):
    model = WorkPlace
    success_url = reverse_lazy('users:works')



