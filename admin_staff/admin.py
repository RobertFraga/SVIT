from django.contrib import admin
from admin_staff.models import StudentProfile,Announcement, FacultyStaff, registrarStaff, cashierStaff, section, level, accademicYear, admissionStaff, accountingStaff
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
# Register your models here.

@admin.register(StudentProfile)
class students(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'adviser','section') 
    ordering = ('surname', )
    search_fields = ('surname',)

@admin.register(FacultyStaff)
class faculty(admin.ModelAdmin):
    list_display = ('faculty_staff_id', 'surname', 'first_name', 'section')
    ordering = ('faculty_staff_id', )
    search_fields = ('surname', 'faculty_staff_id')

@admin.register(registrarStaff)
class registrar(admin.ModelAdmin):
    list_display = ('registrar_staff_id', 'surname', 'first_name', 'middle_name')
    ordering = ('registrar_staff_id', )
    search_fields = ('surname', 'registrar_staff_id')

@admin.register(cashierStaff)
class cashier(admin.ModelAdmin):
    list_display = ('cashier_staff_id', 'surname', 'first_name', 'middle_name')
    ordering = ('cashier_staff_id', )
    search_fields = ('surname', 'cashier_staff_id')

@admin.register(accountingStaff)
class faculty(admin.ModelAdmin):
    list_display = ('announting_staff_id', 'surname', 'first_name', 'middle_name')
    ordering = ('announting_staff_id', )
    search_fields = ('surname', 'announting_staff_id')

@admin.register(Announcement)
class announcement(admin.ModelAdmin):
    list_display = ('title', 'event')
    ordering = ('title', )
    search_fields = ('title', )


admin.site.register(level)
#admin.site.register(section)


@admin.register(section)
class section(admin.ModelAdmin):
    list_display = ('section_name', 'level', 'adviser')
    

class SectionInline(admin.TabularInline):  # or StackedInline if you want vertical
    model = section
    extra = 1  # number of empty forms to add

class LevelAdmin(admin.ModelAdmin):
    inlines = [SectionInline]



admin.site.register(accademicYear)
admin.site.register(admissionStaff)
