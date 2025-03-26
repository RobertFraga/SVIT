from django.forms import ModelForm
from django import forms
from .models import Announcement, StudentProfile, FacultyStaff
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class announcementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'event', 'body']
        widgets = {
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
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class facultyForm(ModelForm):
    class Meta:
        model = FacultyStaff
        fields = '__all__'

