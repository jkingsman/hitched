from message.models import Message
from rest_framework import routers, serializers, viewsets
from message.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
