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

    path('faculty-list/', views.faculty_list, name='faculty_list'),
    path('profile/<int:pk>', views.faculty_profile, name='faculty_profile'),
    path('addflt', views.addstfaculty, name='addflt'),
    path('chart', views.chart, name='chart'),




    path('record', views.accademic_record, name='record'),
    path('finance', views.financial_record, name='financ'),
    path("anecdotal", views.anecdotal_record, name="anecdotal"),















    #accounting board
    path("financial", views.financial_record, name="financialrecord"),

    #student board
    path('student', views.student_dashboard, name='student'),
    path('profile', views.student_profile, name='student-profile'),
    path('grades', views.student_grades, name='student-grades'),



    #faculty board
    path('faculty', views.faculty_dashboard, name='faculty'),
    path('advisory', views.advisory, name='advisory'),
    path('info/<int:pk>', views.student_info, name='info'),
    path('adviser', views.faculty_info, name='faculty_info'),
    path('attendance', views.attendance_record, name="attendance"),

    #accounting
    path('accounting', views.accounting_dashboard, name='accounting' ),
    
]