from django.shortcuts import HttpResponse

# Create your views here
def home(request):
    return HttpResponse("Welcome to the Student Collaboration Home Page!")
