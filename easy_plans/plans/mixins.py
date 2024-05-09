from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, View, CreateView
from django.db.models import Model

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


class YearObjectUpdateMixin(LoginRequiredMixin, UpdateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.object.year
        return context

    def get_success_url(self):
        return reverse_lazy(
            'plans:year_update',
            kwargs={'year_id': self.object.year.pk}
        )


class YearObjectDeleteMixin(LoginRequiredMixin, View):
    pk_kwargs_name: str = ''
    model: Model = None

    def has_permission(self):
        obj = self.get_object()
        return obj.year.plan.student.work_place.user == self.request.user

    def get_object(self):
        model_obj = get_object_or_404(
            self.model,
            pk=self.kwargs.get(self.pk_kwargs_name)
        )
        return model_obj

    def get(self, *args, **kwargs):
        obj = self.get_object()
        if self.has_permission():
            obj.delete()
        return HttpResponseRedirect(
            reverse_lazy(
                'plans:year_update',
                kwargs={'year_id': obj.year.pk}
            )
        )


class YearObjectCreateMixin(LoginRequiredMixin, CreateView):
    year_id_kwarg = 'year_id'

    def get_success_url(self):
        return reverse_lazy(
            'plans:year_update',
            kwargs={self.year_id_kwarg: self.year.pk}
        )

    @property
    def year(self):
        return Year.objects.get(pk=int(self.kwargs.get(self.year_id_kwarg)))

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.year = self.year
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.year
        return context






