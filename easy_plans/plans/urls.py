from django.urls import path

from . import views

app_name = 'plans'

urlpatterns = [
    path('update/<int:student_pk>', views.PlanUpdateView.as_view(), name='update'),
    path('list/', views.PlanList.as_view(), name='list')
]
