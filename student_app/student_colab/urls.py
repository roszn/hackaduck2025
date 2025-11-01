from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.get_user_input, name='get_user_input'),
    path('', views.home, name='home'),  # Handles the root URL
    path('sign_in/', views.sign_in, name='sign_in'),
    path('profile/', views.profile, name='profile'),
]  