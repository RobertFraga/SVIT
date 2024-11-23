from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class accademicYear(models.Model):
    accademicYear = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.accademicYear

class subject(models.Model):
    subjectname = models.CharField(max_length=30, null=True, blank=True)
    subject_discripiton = models.CharField(max_length=30, null=True, blank=True)
    subject_grade_firstQ = models.IntegerField(null=True, blank=True)
    subject_grade_secondQ = models.IntegerField(null=True, blank=True)
    subject_grade_thirdQ = models.IntegerField(null=True, blank=True)
    subject_grade_fourthQ = models.IntegerField(null=True, blank=True)
    average = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.subjectname

class level(models.Model):
    level = models.CharField(max_length=20);
    
    def __str__(self):
        return self.level


class section(models.Model):
    section_name = models.CharField(max_length=20)
    level = models.ForeignKey("level", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.section_name



class FacultyStaff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    faculty_staff_id = models.BigIntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    sufix = models.CharField(max_length=24, blank=True, null=True)

    
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, default="Gender", choices=gender_choice, null=True)
    
    civil_choice = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )
    civil_status = models.CharField(max_length=10, default="Status", choices=civil_choice, blank=True, null=True)

    birth_date = models.DateField(null=True)
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=24, blank=True, null=True)

    contact = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    section = models.OneToOneField('section', blank=True, null=True, on_delete=models.SET_NULL)
    subject = models.OneToOneField('subject', blank=True, null=True, on_delete=models.SET_NULL)

    
    class Meta:
        managed = True
        db_table = 'faculty_staff'

    def __str__(self):
        return self.surname

    
    

class StudentProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    student_lrn = models.BigIntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    sufix = models.CharField(max_length=24, blank=True, null=True)

    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=24, default="Gender", choices=gender_choice, blank=True, null=True)

    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=24, blank=True, null=True)

    civil_choice = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )
    civil_status = models.CharField(max_length=10, default="Status", choices=civil_choice, blank=True, null=True)
    
    contact = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    
    section = models.ForeignKey('section', null=True, on_delete=models.SET_NULL)
    adviser = models.ForeignKey('FacultyStaff', blank=True, null=True, on_delete=models.SET_NULL)
    level = models.ForeignKey('level', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = True
        db_table = 'student_profile'
    
    def __str__(self):
        return self.surname




class Announcement(models.Model):
    announcement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    event = models.DateField(null=True)

    class Meta:
        managed = True
        db_table = 'annoucement'
    
    def __str__(self):
        return self.title
    

class registrarStaff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    registrar_staff_id = models.BigIntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    sufix = models.CharField(max_length=24, blank=True, null=True)

    
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, default="Gender", choices=gender_choice, null=True)
    
    civil_choice = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )
    civil_status = models.CharField(max_length=10, default="Status", choices=civil_choice, blank=True, null=True)

    birth_date = models.DateField(null=True)
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=24, blank=True, null=True)

    contact = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    
    def __str__(self):
        return self.surname

class guidanceStaff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    guidance_staff_id = models.BigIntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    sufix = models.CharField(max_length=24, blank=True, null=True)

    
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, default="Gender", choices=gender_choice, null=True)
    
    civil_choice = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )
    civil_status = models.CharField(max_length=10, default="Status", choices=civil_choice, blank=True, null=True)

    birth_date = models.DateField(null=True)
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=24, blank=True, null=True)

    contact = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    
    def __str__(self):
        return self.surname


class cashierStaff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cashier_staff_id = models.BigIntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    sufix = models.CharField(max_length=24, blank=True, null=True)

    
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, default="Gender", choices=gender_choice, null=True)
    
    civil_choice = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )
    civil_status = models.CharField(max_length=10, default="Status", choices=civil_choice, blank=True, null=True)

    birth_date = models.DateField(null=True)
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=24, blank=True, null=True)

    contact = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    
    def __str__(self):
        return self.surname

class admissionStaff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    admission_staff_id = models.BigIntegerField(primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    sufix = models.CharField(max_length=24, blank=True, null=True)

    
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, default="Gender", choices=gender_choice, null=True)
    
    civil_choice = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    )
    civil_status = models.CharField(max_length=10, default="Status", choices=civil_choice, blank=True, null=True)

    birth_date = models.DateField(null=True)
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=24, blank=True, null=True)

    contact = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    
    def __str__(self):
        return self.surname
