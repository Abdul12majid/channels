from . import views
from django.urls import path

urlpatterns = [
    path("login", views.login_user, name='login-user'),
    path("profile/<str:pk>", views.profile, name='profile'),
    path("verify_log_details", views.verify_log_details, name='verify_log_details'),
    path("verify_reg_details", views.verify_reg_details, name='verify_reg_details'),
    path("register", views.register, name='register'),
    
    
]
