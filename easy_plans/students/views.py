from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from plans.models import Plan
from users.models import Student, WorkPlace
from .forms import StudentCreateForm


class CreateStudent(CreateView, LoginRequiredMixin):
    model = Student
    form_class = StudentCreateForm
    template_name = 'students/student_create_form.html'

    def __create_plan_of_student(self):
        plan = Plan()
        plan.student = self.object
        plan.save()

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['work_place'].queryset = WorkPlace.objects.filter(user=self.request.user)
        return form

    def get_success_url(self):
        self.__create_plan_of_student()
        return reverse_lazy(
            "students:list",
            kwargs={'work_id': self.object.work_place.id}
        )


class StudentsListView(ListView, LoginRequiredMixin):
    model = Student
    template_name = 'students/list.html'

    @property
    def _work_place(self):
        try:
            return WorkPlace.objects.get(id=self.kwargs.get('work_id'))
        except:
            return HttpResponseNotFound("Школа не найдена")

    def get_queryset(self):
        query = Student.objects.filter(
            work_place__id=int(self.kwargs.get('work_id'))
        )
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['school_name'] = self._work_place.school.name
        return context


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentCreateForm
    template_name = 'students/update.html'

    def get_success_url(self):
        return reverse_lazy(
            "students:update",
            kwargs={'pk': self.object.pk}
        )


class StudentDeleteView(DeleteView, LoginRequiredMixin):
    model = Student
    template_name = 'students/student_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(
            "students:list",
            kwargs={'work_id': self.object.work_place.id}
        )


