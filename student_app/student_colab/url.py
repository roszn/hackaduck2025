from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    path('input/', views.get_user_input, name='get_user_input'),
=======
app_name = 'student_colab'
urlpatterns = [
    path('', views.home, name='home'),  # Handles the root URL
    path('student_colab/', views.home, name='student_colab'),
>>>>>>> 3acf5cfe946606ae718da517462e257cee0fb593
]