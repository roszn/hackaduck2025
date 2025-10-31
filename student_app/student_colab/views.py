from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Module
def get_user_input(request):
    if request.method == 'POST':
        # Get the user input from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        course = request.POST.get('course')
        modules = request.POST.getlist('modules')
        
        # Create student
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            course=course
        )
        
        # Create and add modules
        for module_name in modules:
            if module_name.strip():
                module, created = Module.objects.get_or_create(
                    module_name=module_name.strip(),
                    defaults={'module_code': module_name[:10], 'description': ''}
                )
                student.modules.add(module)
        
        return HttpResponse(f"Student {first_name} {last_name} saved successfully!")
    
    # If it's a GET request, show the form
    return render(request, 'student_colab/input_form.html')

def home(request):
    return HttpResponse("Welcome to the Student Collaboration Home Page!")
