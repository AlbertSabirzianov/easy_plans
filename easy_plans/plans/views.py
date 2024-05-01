from typing import Sequence

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, View, CreateView

from plans.models import Plan, Year
from users.models import Student


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


class YearDelete(View, LoginRequiredMixin):

    def get_success_url(self):
        return reverse_lazy(
            'plans:update',
            kwargs={'student_pk': self.year.plan.pk}
        )

    def __get_year(self):
        self.year = Year.objects.filter(
            pk=int(self.kwargs.get('year_id'))
        ).first()
        if not self.year:
            raise Http404()
        return self.year

    def get(self, request, year_id):
        self.__get_year().delete()
        return HttpResponseRedirect(self.get_success_url())


class YearCreateView(CreateView, LoginRequiredMixin):
    """
    TODO: update and saving with modelformset Concert, Exam, Quarter
    """

    model = Year
    template_name = 'plans/year_create_form.html'
    fields = ('start_year', 'end_year', 'result', 'characteristic')

    def __get_plan(self) -> Plan:
        plan = Plan.objects.filter(
            pk=int(self.kwargs.get('plan_id'))
        ).first()
        if not plan:
            raise Http404()
        return plan

    def form_valid(self, form):
        form.instance.plan = self.__get_plan()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'plans:update',
            kwargs={'student_pk': self.__get_plan().pk}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan_id'] = self.kwargs.get('plan_id')
        return context


class YearUpdateView(UpdateView, LoginRequiredMixin):
    """
    TODO: update and saving with modelformset Concert, Exam, Quarter
    """
    model = Year
    fields = ('start_year', 'end_year', 'result', 'characteristic')
    pk_url_kwarg = 'year_id'


