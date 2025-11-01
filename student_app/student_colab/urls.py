from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('input/', views.get_user_input, name='get_user_input'),
    path('matches/<str:student_id>/', views.find_matches, name='find_matches'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
=======
    path('', views.home, name='home'),  # Handles the root URL
    path('sign_in/', views.sign_in, name='sign_in'),
    path('profile/', views.profile, name='profile'),
     path('input/', views.get_user_input, name='get_user_input')
>>>>>>> 4a09711b50764fc7680222e12445375f6ac2476d
]  