from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def get_user_input(request):
    if request.method == 'POST':
        # Get the user input from the form
        user_firstname = request.POST.get('user_firstname')
        # Create a new student (you'll need to add more fields to your form)
        # Student.objects.create(first_name=user_firstname)
        return HttpResponse(f"You entered: {user_firstname}")
    
    # If it's a GET request, show the form
    return render(request, 'student_colab/input_form.html')

def home(request):
    return HttpResponse("Welcome to the Student Collaboration Home Page!")