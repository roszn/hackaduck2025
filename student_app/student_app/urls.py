
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', lambda request: redirect('student/input/')),
    path('admin/', admin.site.urls),
    path('', include('student_colab.url')),

]
