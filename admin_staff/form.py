from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Announcement, StudentProfile, FacultyStaff, payment
from django_select2.forms import ModelSelect2Widget
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
        fields = ['level', 'section', 'adviser']
        exclude = ['user']
        widgets = {
            'level': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'adviser': forms.Select(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.RadioSelect
        }
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        try:
            age = int(age)
        except (ValueError, TypeError):
            raise forms.ValidationError("Age must be a number.")

        if age < 0 or age > 99:
            raise forms.ValidationError("Age must be between 0 and 99.")

        return age



class UserForm(UserCreationForm):
    username = forms.CharField(
        max_length=11,
        min_length=11,
        label='Username',
        required=True,
        error_messages={
            'required': 'Username is required.',
            'max_length': 'Username must be exactly 11 digits.',
            'min_length': 'Username must be exactly 11 digits.'
        },
        help_text='Enter exactly 11 digits.',
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if not re.fullmatch(r'\d{11}', username):
            raise forms.ValidationError("Username must be exactly 11 digits (numbers only).")
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists. Please choose a different one.")
        
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



class paymentForm(ModelForm):
    class Meta:
        model = payment
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_type': forms.Select(attrs={'class': 'form-control'}),
            'reference_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


