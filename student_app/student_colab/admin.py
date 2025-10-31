from django.contrib import admin
from .models import Student, Module, stu_match

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'course', 'email')
    search_fields = ('first_name', 'last_name', 'student_id', 'email', 'course')
    list_filter = ('course',)
    filter_horizontal = ('modules',)
    
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('module_code', 'module_name')
    search_fields = ('module_code', 'module_name')
    
class StuMatchAdmin(admin.ModelAdmin):
    list_display = ('student1', 'student2', 'module', 'status', 'created_at')
    search_fields = ('student1__first_name', 'student1__last_name', 'student2__first_name', 'student2__last_name')
    list_filter = ('status', 'module')

admin.site.register(Student, StudentAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(stu_match, StuMatchAdmin)