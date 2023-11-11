from django.shortcuts import render, get_object_or_404
from .models import Chat, Contact
from apps.message.models import Message
from rest_framework.viewsets import ModelViewSet
from apps.message.serializers import MessageSerializer, MessageCreateSerializer, MessageDetailSerializer, \
    MessageListSerializer
from apps.users.models import User


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return MessageCreateSerializer
        elif self.action in ("update", "partial_update"):
            return MessageDetailSerializer
        elif self.action == "list":
            return MessageListSerializer
        elif self.action == "retrieve":
            return MessageDetailSerializer
        return self.serializer_class


def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by('-timestamp').all()[:10]


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)


def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)


def index(request):
    return render(request, 'index.html')
