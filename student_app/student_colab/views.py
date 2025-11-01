from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def get_user_input(request):
    if request.method == 'POST':
        # Get the user input from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        return HttpResponse(f"Name: {first_name} {last_name}, Student ID: {student_id}")
    
    # If it's a GET request, show the form
    return render(request, 'student_colab/input_form.html')

def home(request):
    return render(request, "student_colab/home.html")

def sign_in(request):
    return render(request, "student_colab/login.html")

def profile(request):
    return render(request, "student_colab/profile.html")