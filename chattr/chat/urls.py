from django.urls import path

import chat.views

urlpatterns = [
    path('<str:room_name>/', chat.views.room, name='index'),
]
