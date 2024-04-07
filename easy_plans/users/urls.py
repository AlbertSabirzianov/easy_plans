from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('main/', views.MainPage.as_view(), name='main'),
    path("registration/", views.UserCreateView.as_view(), name='registration'),
    path("login/", views.UserLoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path("update_person/", views.PersonalPageUpdateView.as_view(), name='update_person'),

    path('works/', views.WorkPlacesView.as_view(), name='works'),
    path('add_work/', views.WorkPlacesAdd.as_view(), name='add_work'),

    path('delete_work/<int:pk>', views.DeleteWorkPlace.as_view(), name='delete_work')
]
