from django.shortcuts import render
from django.http import HttpResponse

def get_user_input(request):
    if request.method == 'POST':
        # Get the user input from the form
        user_firstname = request.POST.get('user_firstname')
        # Do something with the input
        return HttpResponse(f"You entered: {user_firstname}")
    
    # If it's a GET request, show the form
    return render(request, 'student_colab/input_form.html')

def home(request):
    return HttpResponse("Welcome to the Student Collaboration Home Page!")
