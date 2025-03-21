from django.urls import path
from . import views

urlpatterns = [
    #login Page
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    #admin board
    path('', views.admin_dashboard, name='home'),
    path('update_annoucement<str:pk>', views.announcement, name='announcement'),
    path('class/', views.classes, name='classes'),
    path('student/', views.student_list, name='student_list'),
    path('student/<int:pk>', views.student, name='studentinfo'),   
    path('addstudent', views.addstudent, name='addstd'),
    path('student_form', views.student_form, name='student_form'),

    path('faculty-list/', views.faculty_list, name='faculty_list'),
    path('profile/<int:pk>', views.faculty_profile, name='faculty_profile'),
    path('addflt', views.addstfaculty, name='addflt'),
    path('chart', views.chart, name='chart'),
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

    #cashier end
    path('cashier-dashboard', views.cashier_dashboard, name='cashier'),
    
    #admission
    path('admission-dashboard', views.admission_dashboard, name='admission'),
    
]