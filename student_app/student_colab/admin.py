from django.contrib import admin

# Register your models here.
from .models import Student, Module, stu_match
# Registering the Student model with custom admin options

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'email', 'stu_year', 'module')
    search_fields = ('first_name', 'last_name', 'student_id', 'email')
    list_filter = ('module', 'stu_year')
    list_display = ('first_name', 'last_name', 'student_id', 'course', 'email')
    search_fields = ('first_name', 'last_name', 'student_id', 'email', 'course')
    list_filter = ('course',)
    filter_horizontal = ('modules',)

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('module_code', 'module_name')
    search_fields = ('module_code', 'module_name')
    fieldsets = [
        ("Module Details", {
            'fields': ['module_code', 'module_name']
        }),
        ("Additional Information", {
            'fields': ['description']
        })
    ]
    
class StuMatchAdmin(admin.ModelAdmin):
    list_display = ('student1', 'student2', 'module', 'status', 'created_at')
    search_fields = ('student1__first_name', 'student1__last_name', 'student2__first_name', 'student2__last_name', 'module__module_code')
    search_fields = ('student1__first_name', 'student1__last_name', 'student2__first_name', 'student2__last_name')
    list_filter = ('status', 'module')
    

admin.site.register(Student, StudentAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(stu_match, StuMatchAdmin)
admin.site.register(stu_match, StuMatchAdmin)