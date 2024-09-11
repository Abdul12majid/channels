from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("profile/<str:pk>", views.profile, name='profile'),
    
]
