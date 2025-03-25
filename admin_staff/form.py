from django.forms import ModelForm
from django import forms
from .models import Announcement, StudentProfile, FacultyStaff


class announcementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'event', 'body']
        widgets = {
            'event': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

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

