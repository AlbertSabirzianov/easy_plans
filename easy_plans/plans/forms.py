from django.forms import inlineformset_factory, modelformset_factory
from django import forms
from .models import Year, Exam, Concert, Quarter

ExamInlineForm = inlineformset_factory(
    Year,
    Exam,
    fields=('date', 'estimation'),
    widgets={
        'date': forms.DateInput(
            attrs={'type': 'date'}
        )
    }
)

ConcertInlineForm = inlineformset_factory(
    Year,
    Concert,
    fields=('name', 'date'),
    widgets={
        'date': forms.DateInput(
            attrs={'type': 'date'}
        )
    }
)

QuarterInlineForm = inlineformset_factory(
    Year,
    Quarter,
    fields=('number', 'repertoire', 'performance', 'estimation'),
    max_num=4
)


class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = ('date', 'estimation')
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }


class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = ('name', 'date')
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

