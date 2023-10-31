from django.urls import path
from apps.message import views

urlpatterns = [
    path('chat/', views.index, name='index'),
    path("chat/<str:room_name>/", views.room, name="room"),
]


