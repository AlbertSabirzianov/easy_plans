from django.urls import path

from .views import hello

app_name = 'users'

urlpatterns = [
    path('hello/', hello)
]
