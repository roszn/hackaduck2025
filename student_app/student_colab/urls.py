from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.get_user, name='get_user_firstname'),
]  