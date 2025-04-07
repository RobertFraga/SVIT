from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Announcement, StudentProfile, FacultyStaff
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
import re


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
            'status': forms.RadioSelect
        }
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 0 or age > 99:
            raise forms.ValidationError("Age must be between 0 and 99.")
        return age  



class UserForm(UserCreationForm):
    username = forms.CharField(
        max_length=11,
        min_length=11,
        label='Phone Number',
        help_text='Enter exactly 11 digits.',
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.fullmatch(r'\d{11}', username):
            raise forms.ValidationError("Username must be exactly 11 digits (numbers only).")
        return username

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }

class facultyForm(ModelForm):
    class Meta:
        model = FacultyStaff
        fields = '__all__'

