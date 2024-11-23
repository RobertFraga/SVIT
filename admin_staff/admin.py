from django.contrib import admin
from admin_staff.models import StudentProfile,Announcement, FacultyStaff, guidanceStaff, registrarStaff, cashierStaff, section, level, subject, accademicYear, admissionStaff, accountingStaff

# Register your models here.

@admin.register(StudentProfile)
class students(admin.ModelAdmin):
    list_display = ('student_lrn', 'surname', 'first_name', 'adviser','section') 
    ordering = ('student_lrn', )
    search_fields = ('surname', 'student_lrn')


@admin.register(FacultyStaff)
class faculty(admin.ModelAdmin):
    list_display = ('faculty_staff_id', 'surname', 'first_name', 'section')
    ordering = ('faculty_staff_id', )
    search_fields = ('surname', 'faculty_staff_id')


@admin.register(registrarStaff)
class faculty(admin.ModelAdmin):
    list_display = ('registrar_staff_id', 'surname', 'first_name', 'middle_name')
    ordering = ('registrar_staff_id', )
    search_fields = ('surname', 'registrar_staff_id')


@admin.register(guidanceStaff)
class faculty(admin.ModelAdmin):
    list_display = ('guidance_staff_id', 'surname', 'first_name', 'middle_name')
    ordering = ('guidance_staff_id', )
    search_fields = ('surname', 'guidance_staff_id')


@admin.register(cashierStaff)
class faculty(admin.ModelAdmin):
    list_display = ('cashier_staff_id', 'surname', 'first_name', 'middle_name')
    ordering = ('cashier_staff_id', )
    search_fields = ('surname', 'cashier_staff_id')


admin.site.register(subject)
admin.site.register(section)
@admin.register(level)
class level(admin.ModelAdmin):
    list_display = ('level',  )
    ordering = ('level', )



@admin.register(Announcement)
class announcement(admin.ModelAdmin):
    list_display = ('title', 'event')
    ordering = ('title', )
    search_fields = ('title', )

@admin.register(accountingStaff)
class faculty(admin.ModelAdmin):
    list_display = ('announting_staff_id', 'surname', 'first_name', 'middle_name')
    ordering = ('announting_staff_id', )
    search_fields = ('surname', 'announting_staff_id')


admin.site.register(accademicYear)
admin.site.register(admissionStaff)