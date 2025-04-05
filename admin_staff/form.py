from django.forms import ModelForm
from django import forms
from .models import Announcement, StudentProfile, FacultyStaff
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class announcementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'event', 'body']
        widgets = {
            'event': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'event': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='text-capitalize'),
            Field('body', css_class='text-capitalize')
        )

class studentForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'age': forms.TextInput(
                attrs={
                    'min': 14,
                    'max': 16,
                    'maxlength': '2',
                    'minlength': '2',  
                    'inputmode': 'numeric',  # mobile numeric keyboard
                    'pattern': '[0-9]*',  # numeric only
                    'style': 'appearance: textfield; -moz-appearance: textfield;'  # removes spinners in some browsers
                }
            ),
            'status': forms.RadioSelect
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class facultyForm(ModelForm):
    class Meta:
        model = FacultyStaff
        fields = '__all__'

