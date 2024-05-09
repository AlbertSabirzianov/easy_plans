from django.urls import path

from . import views

app_name = 'plans'

urlpatterns = [
    path('update/<int:student_pk>', views.PlanUpdateView.as_view(), name='update'),

    ### year
    path('year_create/<int:plan_id>', views.YearCreateView.as_view(), name='year_create'),
    path('year_delete/<int:year_id>', views.YearDelete.as_view(), name='year_delete'),
    path('year_update/<int:year_id>', views.YearUpdateView.as_view(), name='year_update'),

    ### exams
    path('exam_delete/<int:exam_id>', views.ExamDeleteView.as_view(), name='exam_delete'),
    path('exam_update/<int:exam_id>', views.ExamUpdateView.as_view(), name='exam_update'),
    path('year_update/<int:year_id>/exam_create', views.ExamCreateView.as_view(), name='exam_create'),

    ### concerts
    path('concert_delete/<int:concert_id>', views.ConcertDeleteView.as_view(), name='concert_delete'),
    path('concert_update/<int:concert_id>', views.ConcertUpdateView.as_view(), name='concert_update'),
    path('year_update/<int:year_id>/concert_create', views.ConcertCreateView.as_view(), name='concert_create'),

    ### quarters
    path('quarter_delete/<int:quarter_id>', views.QuarterDeleteView.as_view(), name='quarter_delete'),
    path('quarter_update/<int:quarter_id>', views.QuarterUpdateView.as_view(), name='quarter_update'),
    path('year_update/<int:year_id>/quarter_create', views.QuarterCreateView.as_view(), name='quarter_create')
]
