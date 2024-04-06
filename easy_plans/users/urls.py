from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('main/', views.MainPage.as_view(), name='main'),
    path("registration/", views.UserCreateView.as_view(), name='registration'),
    path("login/", views.UserLoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout')
]
