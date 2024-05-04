from django.http import Http404
from django.urls import reverse_lazy

from plans import forms
from plans.models import Year, Plan


class YearMixin:
    model = Year
    template_name = 'plans/year_create_form.html'
    fields = ('start_year', 'end_year', 'result', 'characteristic')
    pk_url_kwarg = 'year_id'

    def get_year(self) -> Year:
        self.year = Year.objects.filter(
            pk=int(self.kwargs.get('year_id'))
        ).first()
        if not self.year:
            raise Http404()
        return self.year

    def get_success_url(self):
        return reverse_lazy(
            'plans:update',
            kwargs={'student_pk': self.year.plan.pk}
        )

    def have_permission(self) -> bool:
        return self.request.user == self.year.plan.student.work_place.user

    def get_plan(self) -> Plan:
        plan = Plan.objects.filter(
            pk=int(self.kwargs.get('plan_id'))
        ).first()
        if not plan:
            raise Http404()
        return plan

    @property
    def formsets(self):
        return [
            forms.ExamInlineForm(self.request.POST),
            forms.ConcertInlineForm(self.request.POST),
            forms.QuarterInlineForm(self.request.POST)
        ]

    def save_objects_from_formsets(self):
        for formset in self.formsets:
            for form in formset:
                if form.has_changed() and form.is_valid() and form not in formset.deleted_forms:
                    form.instance.year = self.object
                    form.save()

