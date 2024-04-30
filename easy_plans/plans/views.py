from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView

from plans.models import Plan
from users.models import Student


class PlanUpdateView(UpdateView, LoginRequiredMixin):
    model = Plan
    fields = ('department', 'section')

    def get_success_url(self):
        return reverse_lazy(
            'plans:update',
            kwargs={'student_pk': self.get_object().student.pk}
        )

    def get_object(self, queryset=None) -> Plan:
        student = Student.objects.filter(pk=int(self.kwargs.get('student_pk'))).first()
        if not student:
            raise Http404()
        plan = self.model.objects.filter(
            student=student
        ).first()
        return plan


class PlanList(ListView, LoginRequiredMixin):
    model = Plan

    def get_queryset(self):
        query = self.model.objects.filter(
            student__work_place__user=self.request.user
        )
        return query

