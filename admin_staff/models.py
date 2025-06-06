from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StudentAttendance(models.Model):
    student_lrn = models.ForeignKey('StudentProfile', on_delete=models.CASCADE, db_column='student_lrn')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    class Meta:
        managed = True
        db_table = 'student_attendance'

    def __str__(self):
        return f"Student {self.student_lrn.student_lrn} - {self.date} - {self.status}"
    

class StudentGrade(models.Model):
    student_lrn = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    first_grading = models.FloatField(null=True, blank=True)
    second_grading = models.FloatField(null=True, blank=True)
    third_grading = models.FloatField(null=True, blank=True)
    fourth_grading = models.FloatField(null=True, blank=True)
    final_grade = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_lrn} - {self.subject}"
    

class accademicYear(models.Model):
    starting_year = models.IntegerField(null=True, blank=True)
    ending_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.starting_year

class level(models.Model):
    grade = models.CharField(max_length=20);
    def __str__(self):
        return self.grade


class section(models.Model):
    section_name = models.CharField(max_length=20)
    level = models.ForeignKey(level, on_delete=models.CASCADE, related_name='sections', null=True, blank=True)
    adviser = models.ForeignKey('FacultyStaff', on_delete=models.SET_NULL, null=True, blank=True)

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

    
    class Meta:
        managed = True
        db_table = 'faculty_staff'

    def __str__(self):
        return self.surname

    
    

class StudentProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    student_lrn = models.CharField(max_length=12, primary_key=True)
    surname = models.CharField(max_length=24)
    first_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    sufix = models.CharField(max_length=24, blank=True, null=True)

    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, default=False, choices=gender_choice)

    birth_date = models.DateField(null=True)
    age = models.CharField(null=True, max_length=2)
    birth_place = models.CharField(max_length=50, null=True)
    mother_tongue = models.CharField(max_length=24, null=True)
    ethnic_group = models.CharField(max_length=24, null=True)
    religion = models.CharField(max_length=24, null=True)

    # Adress section
    house_number = models.CharField(max_length=24, null=True)
    streets = models.CharField(max_length=24, null=True)
    barangay = models.CharField(max_length=24, null=True)
    city = models.CharField(max_length=24, null=True)
    province = models.CharField(max_length=24, null=True)
    
    #parent section
    fathers_last_name = models.CharField(max_length=24, null=True)
    fathers_name = models.CharField(max_length=24, null=True)
    fathers_middle_name = models.CharField(max_length=24, null=True)
    mothers_last_name = models.CharField(max_length=24, null=True)
    mothers_name = models.CharField(max_length=24, null=True)
    mothers_middle_name = models.CharField(max_length=24, null=True)
    is_guardian = models.BooleanField(default=False)

    Guardian_Full_Name = models.CharField(max_length=24, blank=True, null=True)

    guardian_or_parent_mobile_number = models.CharField(max_length=11, null=True)

    #document section
    have_Form_137 = models.BooleanField(default=False)
    have_Form_138 = models.BooleanField(default=False)
    have_Good_Moral_Certificate = models.BooleanField(default=False)
    have_PSA = models.BooleanField(default=False)
    

    STATUS_CHOICES = [
        ('transfer_out', 'Transfer Out'),
        ('transfer_in', 'Transfer In'),
        ('dropped', 'Dropped'),
        ('late_enrolee', 'Late Enrolee'),
        ('cct_recipient', 'CCT Recipient'),
        ('balik_aral', 'Balik Aral'),
        ('learner_with_disability', 'Learner with Disability'),
        ('accelerated', 'Accelerated'),
    ]
    
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='transfer_out'
    )


    section = models.ForeignKey('section', blank=True, null=True, on_delete=models.SET_NULL)
    adviser = models.ForeignKey('FacultyStaff', blank=True, null=True, on_delete=models.SET_NULL)
    level = models.ForeignKey('level', blank=True, null=True, on_delete=models.SET_NULL)
    

    class Meta:
        managed = True
        db_table = 'student_profile'
    
    def __str__(self):
        return f"{self.student_lrn}- {self.surname} {self.first_name}" 








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


    def save(self, *args, **kwargs):
        self.title = self.title.capitalize()
        self.body = self.body.capitalize()
        super().save(*args, **kwargs)
    

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


class accountingStaff(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    announting_staff_id = models.BigIntegerField(primary_key=True)
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
    

class payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    student_lrn = models.ForeignKey('StudentProfile', on_delete=models.CASCADE, db_column='student_lrn')
    amount = models.FloatField()
    date = models.DateField()
    payment_options = (
        ('Credit/Debit Card Payment', 'Credit/Debit Card Payment'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Mobile Payment Apps', 'Mobile Payment Apps'),
        ('Office Transaction', 'Office Transaction'),
    )
    payment_type = models.CharField(max_length=50, default="Status", choices=payment_options, blank=True, null=True)

    description = models.TextField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'payment'
    
    def __str__(self):
        return f"Payment {self.payment_id} - {self.student_lrn}"