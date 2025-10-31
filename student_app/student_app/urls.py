from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('student/input/')),
    path('admin/', admin.site.urls),
    path('student/', include('student_colab.urls')),
]