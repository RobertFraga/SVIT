from django.urls import path
from . import views

urlpatterns = [

    path("mark_attendance/", views.mark_attendance, name="mark_attendance"),

    path('fetch-students/', views.fetch_students, name='fetch_students'),
    path('get-grades/<str:student_lrn>/', views.get_student_grades, name='get_student_grades'),

    path('save-grade/', views.save_grade, name='save-grade'),


    # Login Page
    
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # Admin Board
    path('', views.admin_dashboard, name='home'),
    path('update_annoucement<str:pk>', views.announcement, name='announcement'),
    path('class/', views.classes, name='classes'),
    path('student/', views.student_list, name='student_list'),
    path('student/<int:pk>', views.student, name='studentinfo'),
    path('addstudent', views.addstudent, name='addstd'),

    path('faculty-list/', views.faculty_list, name='faculty_list'),
    path('profile/<int:pk>', views.faculty_profile, name='faculty_profile'),
    path('addflt', views.addstfaculty, name='addflt'),
    path('chart', views.chart, name='chart'),

    path('record', views.accademic_record, name='record'),
    path('finance', views.financial_record, name='financ'),
    path("anecdotal", views.anecdotal_record, name="anecdotal"),

    # Accounting Board
    path("financial", views.financial_record, name="financialrecord"),

    # Student Board
    path('student', views.student_dashboard, name='student'),
    path('profile', views.student_profile, name='student-profile'),

    path('grades', views.student_grades, name='student-grades'),
    path('student_attendance_record', views.student_attendance, name='student-attendance'),

    # Faculty Board
    path('faculty', views.faculty_dashboard, name='faculty'),
    path('advisory', views.advisory, name='advisory'),



    path('info/<int:pk>', views.student_info, name='info'),

    path('view_attendance/<int:pk>', views.view_attendance, name='view_attendance'),

   path('api/attendance/<int:pk>/', views.get_attendance_records, name='get_attendance_records'),
   
    path('api/attendance_view_only/<int:pk>/', views.get_attendance_records_view_only, name='get_attendance_records_view_only'),

    


    path('adviser', views.faculty_info, name='faculty_info'),
    path('attendance', views.attendance_record, name="attendance"),
    path('advisory-grades', views.advisory_grades, name="advisory_grades"),

    # Accounting
    path('accounting', views.accounting_dashboard, name='accounting'),

    
]
