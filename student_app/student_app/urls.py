
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.shortcuts import redirect
=======
>>>>>>> 3acf5cfe946606ae718da517462e257cee0fb593

urlpatterns = [
    path('', lambda request: redirect('student/input/')),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('student/', include('student_colab.urls')),
=======
    path('', include('student_colab.url')),

>>>>>>> 3acf5cfe946606ae718da517462e257cee0fb593
]
