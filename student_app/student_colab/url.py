from django.urls import path
from . import views
app_name = 'student_colab'
urlpatterns = [
path('', views.student_colab_view, name='student_colab'),
]