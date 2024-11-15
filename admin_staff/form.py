from django.forms import ModelForm
from .models import Announcement, StudentProfile, FacultyStaff, GuidanceStaff, AdminStaff, AdmissionStaff

class announcementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'body']

class studentForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class facultyForm(ModelForm):
    class Meta:
        model = FacultyStaff
        fields = '__all__'

class guidanceForm(ModelForm):
    class Meta:
        model = GuidanceStaff
        fields = '__all__'

class adminForm(ModelForm):
    class Meta:
        model = AdminStaff
        fields = '__all__'

class admitionForm(ModelForm):
    class Meta:
        model = AdmissionStaff
        fields = '__all__'