from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django_select2 import forms as s2forms

from users.models import WorkPlace, School

User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('email', 'password')


class SchoolWidget(s2forms.ModelSelect2Widget):
    search_fields = ['name__icontains']
    model = School


class WorkAddForm(forms.ModelForm):

    class Meta:
        model = WorkPlace
        fields = ('school',)
        widgets = {
            'school': SchoolWidget
        }

    def save(self, commit=True, request=None):
        self.instance.user = request.user
        self.instance.save()
        return self.instance
