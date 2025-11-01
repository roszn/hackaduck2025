from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Module, stu_match

def get_user_input(request):
    if request.method == 'POST':
        # Get the user input from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        coureses = request.POST.get('course', 'Not Specified')
        modules = request.POST.getlist('modules')
        
        # Create student with error handling
        try:
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                student_id=student_id,
                coureses=coureses,
                email='',
                password='',
                stu_year='2025-01-01'
            )
        except Exception as e:
            return HttpResponse(f"Error creating student: {str(e)}")
        
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
    return render(request, 'student_colab/home.html')

def find_matches(request, student_id):
    try:
        student = Student.objects.get(student_id=student_id)
        matches = stu_match.find_matches(student)
        
        match_info = []
        for match in matches:
            shared_modules = student.modules.filter(id__in=match.modules.all())
            match_info.append({
                'student': match,
                'shared_modules': shared_modules
            })
        
        return render(request, 'student_colab/matches.html', {
            'student': student,
            'matches': match_info
        })
    except Student.DoesNotExist:
        return HttpResponse("Student not found")

def signup(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            Student.objects.create(
                student_id=student_id,
                email=email,
                course='Not Specified'
            )
            return HttpResponse("Account created successfully!")
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
    
    return render(request, 'student_colab/signup.html')