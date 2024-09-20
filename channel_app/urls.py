from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name='index'),
    path("chat/<username>", views.get_or_create_chatroom, name='start_chat'),
    path('chat/room/<chatroom_name>', views.index, name="chatroom")
    
]
