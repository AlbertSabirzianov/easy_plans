from typing import Sequence

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, View, CreateView

from plans.models import Plan, Year, Exam, Concert, Quarter
from users.models import Student
from . import forms
from .forms import ExamForm
from .mixins import YearMixin


class PlanUpdateView(UpdateView, LoginRequiredMixin):
    model = Plan
    fields = ('department', 'section')

    def __get_student(self) -> Student:
        student = Student.objects.filter(pk=int(self.kwargs.get('student_pk'))).first()
        if not student:
            raise Http404()
        return student

    def __get_years(self) -> Sequence[Year]:
        years = Year.objects.filter(
            plan=self.object
        )
        return years

    def get_success_url(self):
        return reverse_lazy(
            'plans:update',
            kwargs={'student_pk': self.get_object().student.pk}
        )

    def get_object(self, queryset=None) -> Plan:
        student = self.__get_student()
        plan = self.model.objects.filter(
            student=student
        ).first()
        return plan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = self.__get_years()
        return context


# years
class YearDelete(YearMixin, View, LoginRequiredMixin):

    def get(self, request, year_id):
        self.get_year()
        if self.have_permission():
            self.year.delete()
        return HttpResponseRedirect(self.get_success_url())


class YearCreateView(YearMixin, CreateView, LoginRequiredMixin):

    def form_valid(self, form):
        form.instance.plan = self.get_plan()
        self.object = form.save()
        self.year = self.object
        self.save_objects_from_formsets()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan_id'] = self.kwargs.get('plan_id')
        context['exam_form'] = forms.ExamInlineForm()
        context['concert_form'] = forms.ConcertInlineForm()
        context['quarter_form'] = forms.QuarterInlineForm()
        return context


class YearUpdateView(UpdateView, LoginRequiredMixin):
    model = Year
    template_name = 'plans/year_update.html'
    fields = ('start_year', 'end_year', 'result', 'characteristic')
    pk_url_kwarg = 'year_id'

    def get_success_url(self):
        return reverse_lazy(
            'plans:year_update',
            kwargs={'year_id': self.object.pk}
        )


# exams
class ExamDeleteView(View, LoginRequiredMixin):

    def get_exam(self):
        exam = Exam.objects.get(
            pk=int(self.kwargs.get('exam_id'))
        )
        if not exam:
            raise Http404()
        return exam

    def has_permission(self):
        exam = self.get_exam()
        print(exam.year.plan.student.work_place.user)
        print(self.request.user)
        return exam.year.plan.student.work_place.user == self.request.user

    def get(self, *args, **kwargs):
        exam = self.get_exam()
        if self.has_permission():
            exam.delete()
        return HttpResponseRedirect(
            reverse_lazy(
                'plans:year_update',
                kwargs={'year_id': exam.year.pk}
            )
        )


class ExamUpdateView(UpdateView, LoginRequiredMixin):
    model = Exam
    pk_url_kwarg = 'exam_id'
    template_name = 'plans/exam_update.html'
    form_class = ExamForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.object.year
        return context

    def get_success_url(self):
        return reverse_lazy(
            'plans:year_update',
            kwargs={'year_id': self.object.year.pk}
        )


class ExamCreateView(CreateView, LoginRequiredMixin):
    model = Exam
    pk_url_kwarg = 'exam_id'
    form_class = ExamForm
    template_name = 'plans/exam_create.html'

    def get_success_url(self):
        return reverse_lazy(
            'plans:year_update',
            kwargs={'year_id': self.year.pk}
        )

    @property
    def year(self):
        return Year.objects.get(pk=int(self.kwargs.get('year_id')))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.year = self.year
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.year
        return context
