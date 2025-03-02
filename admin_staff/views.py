from django.shortcuts import render, redirect
from .models import StudentProfile, FacultyStaff, Announcement
from django.shortcuts import render , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only
from .form import announcementForm, studentForm, facultyForm
# Create your views here.
# JCODE
from django.utils.timezone import now
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import StudentGrade,StudentAttendance







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



@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("invalid username or password, try again"))
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
    announcement = Announcement.objects.get
    context = {'announcement': announcement}
    return render(request, 'admin/admin_dashboard.html', context)

def chart(request):
    return render(request, 'admin/charts.html')

def announcement(request, pk):
    annouce = Announcement.objects.get(announcement_id=pk)
    form = announcementForm(instance=annouce)
    if request.method == 'POST':
        form = announcementForm(request.POST, instance=annouce)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'admin/announcement_form.html', context)


@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def classes(request):
    return render(request, 'admin/classes.html', )

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def student_list(request):
    students = StudentProfile.objects.all()
    return render(request, 'admin/student_list.html', { 'student': students})

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def student(request, pk):
    student = StudentProfile.objects.get(student_lrn = pk)
    return render(request, 'admin/student_profile.html', {'student': student})

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def addstudent(request):
    student = studentForm()
    if request.method == "POST":
        student = studentForm(request.POST)
        if student.is_valid():
            student.save()
            return redirect('/')

    context = {'student': student}
    return render(request, 'admin/addstudent.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def addstfaculty(request):
    faculty = facultyForm()
    if request.method == "POST":
        faculty = facultyForm(request.POST)
        if faculty.is_valid():
            faculty.save()
            return redirect('/')

    context = {'faculty': faculty}
    return render(request, 'admin/addfaculty.html', context)
    



@login_required(login_url='login')
@allowed_user(allow_roles=['admin'])
def faculty_list(request):
    faculty = FacultyStaff.objects.all()
    return render(request, 'admin/faculty_list.html', { 'faculty': faculty})




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

#accounting end
@login_required(login_url='login')
@allowed_user(allow_roles=['accounting'])
def accounting_dashboard(request):
    announcement = Announcement.objects.get
    context = {'announcment': announcement}
    return render(request, "accounting/financial_record.html", context)


#student end
@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_dashboard(request):
    announcement = Announcement.objects.get
    student = request.user.studentprofile
    context = { 'student': student, 'announcement': announcement}
    return render(request, 'student/student_dashboard.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_profile(request):
    student = request.user.studentprofile
    return render(request, 'student/student_profile.html', {'student': student})


@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_grades(request):
    student = request.user.studentprofile
    # return render(request, 'student/grades.html', context)
    return render(request, 'student/grades.html', {'student': student})


@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def student_attendance(request):
    student = request.user.studentprofile
    # return render(request, 'student/grades.html', context)
    return render(request, 'student/view_attendance.html', {'student': student})



#faculty end
@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def faculty_dashboard(request):
    announcement = Announcement.objects.get
    adviser = request.user.facultystaff
    context = {'adviser': adviser, 'announcement': announcement}
    return render(request, 'faculty/faculty-dashboard.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def advisory(request):
    advisoryClass = request.user.facultystaff.studentprofile_set.all()
    adviser = request.user.facultystaff
    context = {'advisoryClass': advisoryClass, 'adviser':adviser}
    return render(request, 'faculty/student_list.html', context)



@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def student_info(request, pk):
    student = StudentProfile.objects.get(student_lrn = pk)
    context = {'student': student}
    return render(request, 'faculty/student_profile.html', context)






@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def get_attendance_records(request, pk):
    student = get_object_or_404(StudentProfile, student_lrn=pk)
    attendance_records = StudentAttendance.objects.filter(student_lrn=student).order_by('-date')

    total_count = attendance_records.count()
    present_count = attendance_records.filter(status="Present").count()
    absent_count = attendance_records.filter(status="Absent").count()

    data = [
        {
            'date': record.date.strftime('%Y-%m-%d'),
            'status': record.status
        } for record in attendance_records
    ]

    return JsonResponse({
        'student_lrn': student.student_lrn,
        'first_name': student.first_name,
        'surname': student.surname,
        'attendance_records': data,
        'total_count': total_count,
        'present_count': present_count,
        'absent_count': absent_count
    })





@login_required(login_url='login')
@allowed_user(allow_roles=['student'])
def get_attendance_records_view_only(request, pk):
    student = get_object_or_404(StudentProfile, student_lrn=pk)
    attendance_records = StudentAttendance.objects.filter(student_lrn=student).order_by('-date')

    total_count = attendance_records.count()
    present_count = attendance_records.filter(status="Present").count()
    absent_count = attendance_records.filter(status="Absent").count()

    data = [
        {
            'date': record.date.strftime('%Y-%m-%d'),
            'status': record.status
        } for record in attendance_records
    ]

    return JsonResponse({
        'student_lrn': student.student_lrn,
        'first_name': student.first_name,
        'surname': student.surname,
        'attendance_records': data,
        'total_count': total_count,
        'present_count': present_count,
        'absent_count': absent_count
    })


@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def view_attendance(request, pk):
    student = StudentProfile.objects.get(student_lrn = pk)
    context = {'student': student}
    return render(request, 'faculty/view_attendance.html', context)


@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def student_records(request):
    return render(request, 'faculty/record.html')


@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def faculty_info(request):
    adviser = request.user.facultystaff
    context = {'adviser': adviser}
    return render(request, 'faculty/faculty_profile.html', context)

@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def attendance_record(request):
    return render(request, 'faculty/attendance_record.html')

@login_required(login_url='login')
@allowed_user(allow_roles=['faculty'])
def advisory_grades(request):
    adviser = request.user.facultystaff
    context = {'adviser': adviser}
    return render(request, 'faculty/advisory_grades.html', context)