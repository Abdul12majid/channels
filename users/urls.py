from . import views
from django.urls import path

urlpatterns = [
    path("login", views.login_user, name='login-user'),
    path("profile/<str:pk>", views.profile, name='profile'),
    path("verify_details", views.verify_details, name='verify_details'),
    path("register", views.register, name='register'),
    
    
]
