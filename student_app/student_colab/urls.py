from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.get_user_input, name='get_user_input'),
    path('matches/<str:student_id>/', views.find_matches, name='find_matches'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
]  