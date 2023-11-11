from django.urls import path, re_path
from apps.message import views

from rest_framework.routers import DefaultRouter

from apps.message.views import MessageViewSet

app_name = 'chat'

router = DefaultRouter()
router.register('message', MessageViewSet, basename='message')

urlpatterns = [
                  path("", views.index, name="index")
              ] + router.urls
