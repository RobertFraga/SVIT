from django.shortcuts import get_object_or_404, render, redirect
from .models import StudentProfile, FacultyStaff, Announcement, registrarStaff, cashierStaff, admissionStaff, StudentGrade,StudentAttendance, accademicYear, level, payment
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only
from .form import announcementForm, studentForm, facultyForm, UserForm, paymentForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.






@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User does not exist")
            return redirect('login')

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Password is incorrect")
            return redirect('login')      
    else:
        context = {}    
        return render(request, 'login/login.html', context )
    

def logout_user(request):
    logout(request)
    return redirect('login')
    

#admin dashboard
@login_required(login_url='login')
@admin_only
def admin_dashboard(request): 
    announcement = Announcement.objects.all().order_by('-announcement_id')
    advisers = FacultyStaff.objects.all()

    context = {'announcement': announcement, 'advisers': advisers}
    return render(request, 'admin/admin_dashboard.html', context)

def add_announcement(request):
    announce = announcementForm()
    if request.method == "POST":
        announce = announcementForm(request.POST)
        if announce.is_valid():
            announce.save()
            return redirect('/')

    context = {'announce': announce}
    return render(request, 'admin/announcement_form.html', context)

def view_announcement(pk):
    announcement = get_object_or_404(Announcement, announcement_id=pk)
    return JsonResponse({
        'title': announcement.title,
        'event': announcement.event,
        'body': announcement.body
    })

def delete_annoucement(request, pk):
    announcement = get_object_or_404(Announcement, announcement_id=pk)
    if  request.method=="POST":
         announcement.delete()
         return redirect('/')
    return render(request,'admin/admin-dashboard.html')


@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def classes(request):
    return render(request, 'admin/classes.html', )

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def student(request, pk):
    student = StudentProfile.objects.get(student_lrn = pk)
    return render(request, 'admin/student_profile.html', {'student': student})

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def addstudent(request):
    student = UserCreationForm()
    if request.method == "POST":
        student = UserCreationForm(request.POST)
        if student.is_valid():
            user = student.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)
            return redirect('/student_form')

    context = {'student': student}
    return render(request, 'admin/addstudent.html', context)



@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def student_form(request):
    student = studentForm()
    if request.method == "POST":
        student = studentForm(request.POST)
        if student.is_valid():
            student.save()
            return redirect('/')

    context = {'student': student}
    return render(request, 'admin/student_form.html', context)
    



@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def faculty_list(request):
    if 'search' in request.GET:
        search = request.GET['search']
        faculty = FacultyStaff.objects.filter(Q(surname__icontains=search) | Q(first_name__icontains=search))
    else:
        faculty = FacultyStaff.objects.all()

    context = {'faculty': faculty}
    return render(request, 'admin/faculty_list.html', context)


@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def add_faculty(request):
    faculty = UserCreationForm()
    if request.method == "POST":
        faculty = UserCreationForm(request.POST)
        if faculty.is_valid():
            user = faculty.save()
            group = Group.objects.get(name='faculty')
            user.groups.add(group)
            return redirect('/faculty_form')

    context = {'faculty': faculty}
    return render(request, 'admin/addfaculty.html', context)



@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def faculty_form(request):
    faculty = facultyForm()
    if request.method == "POST":
        faculty = facultyForm(request.POST)
        if faculty.is_valid():
            faculty.save()
            return redirect('/')

    context = {'faculty': faculty}
    return render(request, 'admin/faculty_form.html', context)



@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def faculty_profile(request, pk):
    faculty = FacultyStaff.objects.get(faculty_staff_id = pk)
    return render(request, 'admin/faculty_profile.html', {'faculty': faculty})






@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def accademic_record(request):
    return render(request, 'admin/academic_record.html')

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def anecdotal_record(request):
    student = StudentProfile.objects.all()
    context = {'student': student}
    return render(request, "admin/anecdotal_record.html", context)

def financial_record(request):
    return render(request, "admin/financial_record.html")

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def payment_history(request):
    return render(request, 'admin/payment_history.html')

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def jhslist_section(request):
    return render(request, 'admin/jhslist_section.html')

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def list_student(request):
    if 'search' in request.GET:
        search = request.GET['search']
        #student = StudentProfile.objects.filter(surname__icontains=search)
        student = StudentProfile.objects.filter(Q(surname__icontains=search) | Q(first_name__icontains=search) | Q(student_lrn__icontains=search))
    else:
        student = StudentProfile.objects.all()


    
    context = {'student': student}
    return render(request, 'admin/list_student.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def adviser_list(request):
    return render(request, 'admin/adviser_list.html')

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def subject_teacher(request):
    return render(request, 'admin/subject_teacher.html')

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def schedules(request):
    return render(request, 'admin/schedule.html')


#accounting end
@login_required(login_url='login')
@allowed_user(allow_roles=['accounting'])
def accounting_dashboard(request):
    announcement = Announcement.objects.get
    context = {'announcement': announcement}
    return render(request, "accounting/accounting_dashboard.html", context)

@login_required(login_url='login')
@allowed_user(allow_roles=['accounting'])
def accounting_profile(request):
    return render(request, "accounting/financial_record.html")




#student end
@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_dashboard(request):
    announcement = Announcement.objects.all().order_by('-announcement_id')
    accademic_year = accademicYear.objects.get
    student = request.user.studentprofile
    context = { 'student': student, 'announcement': announcement, 'accademic_year': accademic_year }
    return render(request, 'student/student_dashboard.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_profile(request):
    accademic_year = accademicYear.objects.get
    student = request.user.studentprofile
    context = {'student': student, 'accademic_year': accademic_year}
    return render(request, 'student/student_profile.html', context)


@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_grades(request):
    student = request.user.studentprofile
    accademic_year = accademicYear.objects.get
    context = {'student': student, 'accademic_year': accademic_year}
    return render(request, 'student/grades.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_schedule(request):
    student = request.user.studentprofile
    accademic_year = accademicYear.objects.get
    context = {'student': student, 'accademic_year': accademic_year}
    return render(request, 'student/class_schedule.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_billings(request):
    student = request.user.studentprofile
    accademic_year = accademicYear.objects.get
    payments = payment.objects.filter(student_lrn=student).order_by('-date')  
    context = {
        'student': student,
        'accademic_year': accademic_year,
        'payments': payments,
    }
    return render(request, 'student/payhistory.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def payment_detail(request, payment_id):
    student = request.user.studentprofile
    accademic_year = accademicYear.objects.get
    payment_bbj = get_object_or_404(payment, pk=payment_id, student_lrn=request.user.studentprofile)
    context = {
        'student': student,
        'payment': payment_bbj,
        'accademic_year': accademic_year,
    }
    return render(request, 'student/payment_detail.html', context)


#faculty end
@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def faculty_dashboard(request):
    announcement = Announcement.objects.all().order_by('-announcement_id')
    accademic_year = accademicYear.objects.get
    adviser = request.user.facultystaff
    advisoryClass = request.user.facultystaff.studentprofile_set.all()
    context = {'adviser': adviser, 'announcement': announcement, 'advisoryClass': advisoryClass, 'accademic_year': accademic_year}
    return render(request, 'faculty/faculty-dashboard.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def advisory(request):
    advisoryClass = request.user.facultystaff.studentprofile_set.all()
    accademic_year = accademicYear.objects.get
    adviser = request.user.facultystaff
    context = {'advisoryClass': advisoryClass, 'adviser':adviser, 'accademic_year': accademic_year}
    return render(request, 'faculty/student_list.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def student_info(request, pk):
    accademic_year = accademicYear.objects.get
    student = StudentProfile.objects.get(student_lrn = pk)
    context = {'student': student, 'accademic_year': accademic_year}
    return render(request, 'faculty/student_profile.html', context)



@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def faculty_info(request):
    adviser = request.user.facultystaff
    accademic_year = accademicYear.objects.get
    context = {'adviser': adviser, 'accedemic_year': accademic_year}
    return render(request, 'faculty/faculty_profile.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def attendance_record(request, pk):
    student = StudentProfile.objects.get(student_lrn = pk)
    accademic_year = accademicYear.objects.get
    context = {'student': student, 'accedmic_year': accademic_year}
    return render(request, 'faculty/attendance_record.html', context)


@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def advisory_grades(request, pk):
    adviser = request.user.facultystaff
    student = StudentProfile.objects.get(student_lrn = pk)
    accademic_year = accademicYear.objects.get
    context = {'adviser': adviser, 'student': student, 'accademic_year': accademic_year}
    return render(request, 'faculty/faculty-student-grade.html', context)



def get_student_grades(request, student_lrn):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # AJAX request check
        grades = StudentGrade.objects.filter(student_lrn=student_lrn)
        
        grades_dict = {
            grade.subject: {
                "first_grading": grade.first_grading,
                "second_grading": grade.second_grading,
                "third_grading": grade.third_grading,
                "fourth_grading": grade.fourth_grading
            }
            for grade in grades
        }
        
        return JsonResponse({"grades": grades_dict})
    
    return JsonResponse({"error": "Invalid request"}, status=400)



@csrf_exempt
@login_required(login_url='login')
@allowed_user(allow_roles=['faculty', 'admin'])
def save_grade(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            lrn = data.get("lrn")
            subject = data.get("subject")
            column = int(data.get("column"))  # Convert column index to integer
            grade = float(data.get("grade"))

            # Hanapin o gumawa ng bagong record
            student_grade, created = StudentGrade.objects.get_or_create(
                student_lrn=lrn, subject=subject
            )

            # I-update ang tamang grading period
            if column == 2:
                student_grade.first_grading = grade
            elif column == 3:
                student_grade.second_grading = grade
            elif column == 4:
                student_grade.third_grading = grade
            elif column == 5:
                student_grade.fourth_grading = grade
            elif column == 6:
                student_grade.final_grade = grade

            student_grade.save()

            return JsonResponse({"status": "success", "message": "Grade saved successfully!"})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    
    return JsonResponse({"status": "error", "message": "Invalid request"})



@csrf_exempt  # Optional: Use only if CSRF token issues occur (not recommended for production)
def mark_attendance(request):
    if request.method == "POST":
        student_lrn = request.POST.get("student_lrn")
        status = request.POST.get("status")

        try:
            student = StudentProfile.objects.get(student_lrn=student_lrn)
            attendance, created = StudentAttendance.objects.update_or_create(
                student_lrn=student,
                date=now().date(),  # Use today's date
                defaults={"status": status}
            )

            return JsonResponse({"success": True, "message": f"Attendance marked as {status}"})
        except StudentProfile.DoesNotExist:
            return JsonResponse({"success": False, "message": "Student not found"}, status=404)
    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)



@login_required(login_url='login')
def fetch_students(request):
    today = now().date()

    # Ensure the logged-in user is a faculty staff
    if hasattr(request.user, 'facultystaff'):
        faculty_staff = request.user.facultystaff
        section = faculty_staff.section  # Get assigned section

        # Get adviser details
        adviser = {
            'surname': faculty_staff.surname,
            'first_name': faculty_staff.first_name,
            'section': section.section_name if section else "No Section"
        }

        # Fetch students in the adviser's section
        if section:
            students = StudentProfile.objects.filter(
                section=section  # Filter by same section
            ).exclude(
                student_lrn__in=StudentAttendance.objects.filter(date=today).values_list('student_lrn', flat=True)
            ).values('student_lrn', 'surname', 'first_name', 'middle_name')
        else:
            students = []
    else:
        students = []
        adviser = None

    return JsonResponse({
        'students': list(students),
        'adviser': adviser
    })
























#registrar end
@login_required(login_url='login')
@allowed_user(allow_roles=['registrar'])
def registrar_dashboard(request):
    registrar = request.user.registrarstaff
    context = {'registrar': registrar}
    return render(request, 'registrar/registrar-dashboard.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['registrar'])
def pending(request):
    return render(request, "registrar/pending.html")

@login_required(login_url='login')
@allowed_user(allow_roles=['registrar'])
def add_to_class(request):
    return render(request, "registrar/add_class.html")

#cashier end
@login_required(login_url='login')
@allowed_user(allow_roles=['cashier'])
def cashier_dashboard(request):
    cashier = request.user.cashierstaff
    announcement = Announcement.objects.all().order_by('-announcement_id')
    context = {'cashier': cashier, 'announcement': announcement}
    return render(request, "cashier/cashier_dashboard.html", context)

@login_required(login_url='login')
@allowed_user(allow_roles=['cashier'])
def payment_views(request):
    cashier = request.user.cashierstaff
    payments = payment.objects.select_related('student_lrn').order_by('-date', '-payment_id')
    
    if request.method == "POST":
        payment_form = paymentForm(request.POST)
        if payment_form.is_valid():
            payment_form.save()
            messages.success(request, "Payment record created successfully.")
            return redirect('payment')
        else:
            messages.error(request, "Error creating payment record.")
    else:
        payment_form = paymentForm()

    context = {'cashier': cashier, 'payment_form': payment_form, 'payment': payments}
    return render(request, "cashier/payment.html", context)


def delete_payment(request, payment_id):
    # Fetch the payment object using the correct model reference
    payment_instance = get_object_or_404(payment, payment_id=payment_id)

    # Handle the deletion only on POST request
    if request.method == 'POST':
        payment_instance.delete()  # Delete the payment object
        messages.success(request, "Payment record deleted successfully.")
        return redirect('payment')  # Redirect to the list of payments after deletion
    
    # Optionally render the payment detail for confirmation (this can be omitted if not needed)
    context = {'payment': payment_instance}
    return render(request, "cashier/payment.html", context)

@login_required(login_url='login')
@allowed_user(allow_roles=['cashier'])
def details(request, payment_id):
    cashier = request.user.cashierstaff
    
    payment_instance = get_object_or_404(payment, pk=payment_id)
    context = { 'cashier': cashier, 'payment': payment_instance }
    return render(request, "cashier/details.html", context)


#admission end
@login_required(login_url='login')
@allowed_user(allow_roles=['admission'])
def admission_dashboard(request):
    announcement = Announcement.objects.all().order_by('-announcement_id')
    admission = request.user.admissionstaff
    context = {'admission': admission, 'announcement': announcement}
    return render(request, 'admission/admission-dashboard.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['admission'])
def admission_enrollies(request):
    enrollies = StudentProfile.objects.all()
    admission = request.user.admissionstaff
    context = {'enrollies': enrollies, 'admission': admission}
    return render(request, 'admission/enrollies.html', context)


@login_required(login_url='login')
@allowed_user(allow_roles=['admission'])
def admission_student_profile(request, pk):
    admission = request.user.admissionstaff
    student = StudentProfile.objects.get(student_lrn = pk)
    context = {'student': student, 'admission': admission}
    return render(request, 'admission/admission-student-profile.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['admission'])
def admission_student_form(request):
    admission = request.user.admissionstaff
    # student = studentForm()
    # user = UserForm()
    if request.method == "POST":
        student_form = studentForm(request.POST)
        user_form = UserForm(request.POST)

        if student_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()

            # Assign the created user to the student profile
            student = student_form.save(commit=False)
            student.user = user  # ✅ Automatically assign the user
            student.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)

            return redirect('enrollies')
        
        else:
            pass
    
    else:
        student_form = studentForm()
        user_form = UserForm()

    context = {'student': student_form, 'admission': admission, 'user': user_form}
    return render(request, 'admission/admission-student-form.html', context)