from django.urls import path

from . import views

app_name = 'students'

urlpatterns = [
   path('create/', views.CreateStudent.as_view(), name='create'),
   path('list/<int:work_id>/', views.StudentsListView.as_view(), name='list'),
   path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update'),
]
