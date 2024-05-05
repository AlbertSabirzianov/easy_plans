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
    path('year_update/<int:year_id>/exam_create', views.ExamCreateView.as_view(), name='exam_create')
    # """
    # добавление Exam, Concert, Quarter
    # удаление Exam, Concert, Quarter
    # редактирование Exam, Concert, Quarter
    # просмотр Year
    # """
]
