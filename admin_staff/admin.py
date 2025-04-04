from django.contrib import admin
from admin_staff.models import StudentProfile,Announcement, FacultyStaff, guidanceStaff, registrarStaff, cashierStaff, section, level, accademicYear, admissionStaff, accountingStaff
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
# Register your models here.

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'surname', 'student_lrn')

admin.site.register(StudentProfile, StudentProfileAdmin)


# @admin.register(StudentProfile)
# class students(ImportExportModelAdmin):
#     list_display = ('surname', 'first_name', 'adviser','section') 
#     ordering = ('surname', )
#     search_fields = ('surname',)

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


admin.site.register(level)
admin.site.register(section)



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



""" class ProfileInline(admin.StackedInline):
    model = StudentProfile

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]

# Register your models here.
admin.site.unregister(User)

admin.site.register(User, UserAdmin) """