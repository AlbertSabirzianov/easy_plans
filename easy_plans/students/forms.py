from django import forms

from users.models import Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'start_study': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'end_study': forms.DateInput(
                attrs={'type': 'date'}
            )
        }