<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse

def get_user_input(request):
    if request.method == 'POST':
        # Get the user input from the form
        user_input = request.POST.get('user_input')
        # Do something with the input
        return HttpResponse(f"You entered: {user_input}")
    
    # If it's a GET request, show the form
    return render(request, 'student_colab/input_form.html')
=======
from django.shortcuts import HttpResponse

# Create your views here
def home(request):
    return HttpResponse("Welcome to the Student Collaboration Home Page!")
>>>>>>> 3acf5cfe946606ae718da517462e257cee0fb593
