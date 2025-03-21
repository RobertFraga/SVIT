from django.forms import ModelForm
from .models import Announcement, StudentProfile, FacultyStaff

class announcementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'

class studentForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class facultyForm(ModelForm):
    class Meta:
        model = FacultyStaff
        fields = '__all__'

