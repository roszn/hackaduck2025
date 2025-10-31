from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.get_user_input, name='get_user_input'),
]  