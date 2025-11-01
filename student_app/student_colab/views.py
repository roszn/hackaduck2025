from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student, Module
from django.contrib import messages

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            form.save_m2m()  # Save the many-to-many data for the form
            messages.success(request, 'Student registered successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()
    
    return render(request, 'student_colab/student_form.html', {'form': form})

"""def get_user_input(request):
    if request.method == 'POST':
        # Get the user input from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        return HttpResponse(f"Name: {first_name} {last_name}, Student ID: {student_id}")
    
    # If it's a GET request, show the form
    return render(request, 'student_colab/input_form.html')"""

def home(request):
    return render(request, "student_colab/home.html")

def sign_in(request):
    return render(request, "student_colab/login.html")

def profile(request):
    return render(request, "student_colab/profile.html")