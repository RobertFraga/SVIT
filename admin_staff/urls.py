from django.urls import path
from . import views

urlpatterns = [
    #login Page
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    #admin board
    path('', views.admin_dashboard, name='home'),
    #path('update_annoucement<str:pk>', views.announcement, name='announcement'),
    path('add_announcement', views.add_announcement, name='add_announcement'),
    path('announcement/<int:pk>/', views.view_announcement, name='view_announcement'),
    path('delete_announcement/<int:pk>/', views.delete_annoucement, name='delete_announcement'),
    path('class/', views.classes, name='classes'),
    path('student/<int:pk>', views.student, name='studentinfo'),   
    path('addstudent', views.addstudent, name='addstd'),
    path('student_form', views.student_form, name='student_form'),

    path('faculty-list/', views.faculty_list, name='faculty_list'),
    path('profile/<int:pk>', views.faculty_profile, name='faculty_profile'),
    path('addfaculty', views.add_faculty, name='addfaculty'),
    path('facultyform', views.faculty_form, name='facultyform'),
    



    path('payment-history', views.payment_history, name='payment-history'),
    path("list-sections", views.jhslist_section, name="jhslist_section"),
    path('list-students', views.list_student, name="list_student"),
    path('list-adviser', views.adviser_list, name="adviser_list"),
    path('subject-teacher', views.subject_teacher, name="subject_teacher"),
    path('student-schedules', views.schedules, name="scheduler"),

    path('record', views.accademic_record, name='record'),
    path('finance', views.financial_record, name='financ'),
    path("anecdotal", views.anecdotal_record, name="anecdotal"),



    #accounting board
    path("financial", views.financial_record, name="financialrecord"),


    
    #student board
    path('student', views.student_dashboard, name='student'),
    path('profile', views.student_profile, name='student-profile'),
    path('grades', views.student_grades, name='student-grades'),
    path('schedule', views.student_schedule, name='student-schedule'),
    path('billings', views.student_billings, name='student-payment-history'),



    #faculty board
    path('faculty', views.faculty_dashboard, name='faculty'),
    path('advisory', views.advisory, name='advisory'),
    path('info/<int:pk>', views.student_info, name='info'),
    path('adviser', views.faculty_info, name='faculty_info'),
    path('attendance/<int:pk>', views.attendance_record, name="attendance"),
    path('advisory-grades/<int:pk>', views.advisory_grades, name="advisor-grades"),


    path("mark_attendance/", views.mark_attendance, name="mark_attendance"),

    path('fetch-students/', views.fetch_students, name='fetch_students'),
    path('get-grades/<str:student_lrn>/', views.get_student_grades, name='get_student_grades'),

    path('save-grade/', views.save_grade, name='save-grade'),








    #accounting
    path('accounting', views.accounting_dashboard, name='accounting' ),

    #registrar end
    path('registrar-dashboard', views.registrar_dashboard, name='registrar'),
    path('pending-list', views.pending, name='pending'),
    path('add-to-class', views.add_to_class, name='add_class'),

    #cashier end
    path('cashier-dashboard', views.cashier_dashboard, name='cashier'),
    path('student-payment-record', views.payment_views, name='payment'),
    path('edit-payment-record', views.edit_payment, name='edit_payment'),
    
    #admission
    path('admission-dashboard', views.admission_dashboard, name='admission'),
    path('admission-enrollies', views.admission_enrollies, name='enrollies'),
    path('admission_student_profile/<int:pk>', views.admission_student_profile, name='admission_student_profile'),
    path('admission-student-form', views.admission_student_form, name='admission_student_form'),   
]