from django.urls import path

from . import views

app_name = 'plans'

urlpatterns = [
    path('update/<int:student_pk>', views.PlanUpdateView.as_view(), name='update'),
    path('year_create/<int:plan_id>', views.YearCreateView.as_view(), name='year_create'),
    path('year_delete/<int:year_id>', views.YearDelete.as_view(), name='year_delete')
]
