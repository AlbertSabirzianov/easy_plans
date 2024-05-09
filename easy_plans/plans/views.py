from typing import Sequence

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, View, CreateView

from plans.models import Plan, Year, Exam, Concert, Quarter
from users.models import Student
from . import forms
from .forms import ExamForm, ConcertForm
from .mixins import YearMixin, YearObjectUpdateMixin, YearObjectDeleteMixin, YearObjectCreateMixin


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
class ExamDeleteView(YearObjectDeleteMixin):
    model = Exam
    pk_kwargs_name = 'exam_id'


class ExamUpdateView(YearObjectUpdateMixin):
    model = Exam
    pk_url_kwarg = 'exam_id'
    template_name = 'plans/exam_update.html'
    form_class = ExamForm


class ExamCreateView(YearObjectCreateMixin):
    model = Exam
    form_class = ExamForm
    template_name = 'plans/exam_create.html'


# concerts
class ConcertDeleteView(YearObjectDeleteMixin):
    model = Concert
    pk_kwargs_name = 'concert_id'


class ConcertUpdateView(YearObjectUpdateMixin):
    model = Concert
    template_name = 'plans/concert_update.html'
    pk_url_kwarg = 'concert_id'
    form_class = ConcertForm


class ConcertCreateView(YearObjectCreateMixin):
    model = Concert
    form_class = ConcertForm
    template_name = 'plans/concert_create.html'


# quarters
class QuarterDeleteView(YearObjectDeleteMixin):
    model = Quarter
    pk_kwargs_name = 'quarter_id'


class QuarterUpdateView(YearObjectUpdateMixin):
    model = Quarter
    template_name = 'plans/quarter_update.html'
    pk_url_kwarg = 'quarter_id'
    fields = ('number', 'repertoire', 'performance', 'estimation')


class QuarterCreateView(YearObjectCreateMixin):
    model = Quarter
    fields = ('number', 'repertoire', 'performance', 'estimation')
    template_name = 'plans/quarter_create.html'
