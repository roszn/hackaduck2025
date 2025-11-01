from django.urls import path
from . import views
app_name = 'student_colab'
urlpatterns = [
    path('', views.home, name='home'),  # Handles the root URL
    path('student_colab/', views.home, name='student_colab'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('profile/', views.profile, name='profile'),
]