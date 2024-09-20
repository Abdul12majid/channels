from . import views
from django.urls import path

urlpatterns = [
    path("login", views.login_user, name='login-user'),
    path("profile/<str:pk>", views.profile, name='profile'),
    
    
]
